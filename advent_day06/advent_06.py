#############################################################
# IMPORT LIBRARIES

import numpy as np

#############################################################
# READ INPUT FROM FILE

# with open('advent_06_test.txt') as f:		# comment this line to run with actual data
with open('advent_06.txt') as f:				# comment this line to run test
	input = f.readlines()

#############################################################
# PARSE INPUT

# Remove \n from the end each line (except the last)
for i in range(0,np.size(input)-1):
	input[i] = input[i][0:-1]

# Break the string in each row into a list
for i in range(0,np.size(input)):
	input[i] = list(input[i])

#############################################################
# FIND THE MESSAGE FOR MAX FREQUENCY

alphabet = 'abcdefghijklmnopqrstuvwxyz' # create alphabet string for index reference
message = '' # initialize string of message
# Add one to the entry in frequency corresponding to the current letter
for j in range(0,len(input[0])):
	frequency = np.zeros(len(alphabet), dtype=np.int8)
	for i in range(0,len(input)):
		frequency[alphabet.find(input[i][j])] += 1
	message += alphabet[np.argmax(frequency)]
print 'message a: ' + message

#############################################################
# FIND THE MESSAGE FOR MIN FREQUENCY

message = '' # initialize string of message
# Add one to the entry in frequency corresponding to the current letter
for j in range(0,len(input[0])):
	frequency = np.zeros(len(alphabet), dtype=np.int8)
	for i in range(0,len(input)):
		frequency[alphabet.find(input[i][j])] += 1
	message += alphabet[np.argmin(frequency)]
print 'message b: ' + message