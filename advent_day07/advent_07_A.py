#############################################################
# IMPORT LIBRARIES

import numpy as np
from advent_07_functions import checkABBA

#############################################################
# READ INPUT FROM FILE

filename = 'advent_07_test1.txt'	# test case with expected result 2
filename = 'advent_07_test2.txt'	# test case with expected result 1
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
# TEST FOR NUMBER OF TLS-SUPPORTING IPv7 ADDRESSES

countTLS = 0 	# Initializing variable to hold the number of IPs that follow TLS.
				# This value should not be incremented more than once per IP.
for i in range(0,len(input)):
	# Check for ABBA in all the odd segments (the bracketed ones).
	# If ABBA is found, this IP can't TLS, so hypernet will be set to True and countTLS won't be incremented
	j = 1								# start at 1, the first bracketed segment
	numSegments = len(input[i])
	hypernet = False					# initialize hypernet to false
	while j < numSegments:
		if checkABBA(input[i][j]):		# checkABBA on the current segment
			hypernet = True				# set hypernet to true if the segment has ABBA
		j += 2							# increment by two to go to the next bracketed segment
	# Check for ABBA in all the even segments (the nonbracketed ones).
	# If ABBA is found in a nonbracketed segment and hypernet is False (meaning ABBA wasn't found in a bracketed segment), increment countTLS.
	# Break after incrementing countTLS so as not to double increment for a single IP
	j = 0								# start at 0, the first unbracketed segment
	while j < numSegments+1:			
		if checkABBA(input[i][j]) and hypernet == False:
			countTLS += 1				# increment countTLS if a nonbracketed segment as ABBA and none of the hypernet segments did
			break 						# break after incrementing
		j += 2							# increment by two to go the the next unbracketed segment
print countTLS