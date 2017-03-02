#############################################################
# IMPORT LIBRARIES

import numpy as np
from advent_07_functions import *

#############################################################
# READ INPUT FROM FILE

filename = 'advent_07_test3.txt'	# test case with expected result 3
filename = 'advent_07.txt'			# comment this line to run test case
with open(filename) as file:
	input = file.readlines()

#############################################################
# PARSE INPUT

# Remove \n from the end each line (except the last)
for i in range(0,np.size(input)-1):
	input[i] = input[i][0:-1]

# Separate each line into multiple strings
for i in range(0,len(input)):
	curLine = []
	# Count the number of [ in the current line and store its indices
	numOBrackets = 0
	indicesOBrackets, indicesCBrackets = [], []
	for j in range(0,len(input[i])):
		if input[i][j] == '[':
			numOBrackets += 1
			indicesOBrackets.append(j)
		if input[i][j] == ']':
			indicesCBrackets.append(j)
	# Separate each line into strings based on the brackets.
	# Strings inside brackets will retain the brackets for later use.
	indexStart = 0
	for j in range(0,numOBrackets):
		curLine.append(input[i][indexStart:indicesOBrackets[j]])
		curLine.append(input[i][indicesOBrackets[j]:indicesCBrackets[j]+1])
		indexStart = indicesCBrackets[j]+1
	curLine.append(input[i][indexStart:]) # set final segment to the rest (due to odd number of sections)
	# Replace current line's string with array of strings
	input[i] = curLine	

#############################################################
# TEST FOR NUMBER OF SSL-SUPPORTING IPv7 ADDRESSES

countSSL = 0 	# Initializing variable to hold the number of IPs that follow TLS.
for line in range(0,len(input)):
	# Check for ABA in all the segments.
	segment = 0												# start at 0, the first unbracketed segment
	numSegments = len(input[line])
	ABAstrings = []
	while segment < numSegments:
		ABAstrings.append(findABA(input[line][segment]))	# append ABA strings to the list of ABA string
		segment += 2										# increment by 2 to go to next unbracketed segment
	# Check for matching BAB strings in each bracketed segment.
	# If a match is found, increment the number of SSL strings found.
	# Break after incrementing so as not to increment more than once for a single IP.					
	segment = 1
	matched = False											# start at 1, theh first bracketed segment
	while segment < numSegments:
		for ABAsegment in range(0,len(ABAstrings)):
			for ABA in range(0, len(ABAstrings[ABAsegment])):
				if checkBAB(input[line][segment], ABAstrings[ABAsegment][ABA]):
					countSSL += 1							# increment countSSL if a segment follows BAB
					matched = True						 
					break 									# break the first loop after incrementing
			if matched:
				break 										# break the second loop after incrementing
		if matched:
			break 											# break the third loop after incrementing
		segment += 2										# increment by two to go to next bracketed segment
print countSSL