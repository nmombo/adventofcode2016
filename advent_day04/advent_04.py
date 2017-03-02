#############################################################
# IMPORT LIBRARIES

# import numpy
import numpy as np

# import itemgetter for sorting
from operator import itemgetter

# import the functions written in advent_04_functions.py
from advent_04_functions import *

#############################################################
# RECEIVE INPUT CODE

# with open('advent_04_test1.txt') as f:		# comment this line to run with actual data
with open('advent_04.txt') as f:				# comment this line to run test
	input = f.readlines()

#############################################################
# PARSE INPUT CODE

## Remove \n from the end each line (except the last)
for i in range(0,np.size(input)-1):
	input[i] = input[i][0:-1]

# parse everything up to the bracket
presum = []
for i in range(0, np.size(input)):
	curLine = input[i]
	locBracket = curLine.find('[')
	presum.append(curLine[0:locBracket])

# parse the id
id = []
for i in range(0, np.size(input)):
	id.append(int(presum[i][-3:len(presum[i])]))

# parse the room name
name = presum
for i in range(0, np.size(input)):
	name[i] = name[i].replace("-",'')
	name[i] = name[i][0:-3]

# Parse checksum
checksum = input
for i in range(0, np.size(input)):
	locBracket = input[i].find('[')
	checksum[i] = input[i][locBracket+1:-1]

#############################################################
# CHECK FOR VALIDITY OF ROOM

## find the number of instances of each letter in each string
# remove duplicate letters
name_unique = []
for i in range(0, np.size(name)):
	name_unique.append(removeDupliChar(name[i]))
# create parallel array that matches the unique characters with its number of instances
inst = []
for i in range(0, np.size(name_unique)):
	inst.append([])
	for j in range(0, len(name_unique[i])):
		inst[i].append(numInstances(name[i], name_unique[i][j]))

## primary sort by frequency, secondary sort alphabetically
for i in range(0, np.size(name_unique)):
	name_unique[i], inst[i] = [list(x) for x in zip(*sorted(zip(name_unique[i], inst[i]), key=itemgetter(0)))]
	name_unique[i], inst[i] = [list(x) for x in zip(*sorted(zip(name_unique[i], inst[i]), reverse=True, key=itemgetter(1)))]
	name_unique[i] = name_unique[i][0:5]
	name_unique[i] = "".join(name_unique[i])

## count the number of matches between sorted name_unique and checksum
## also store indices of matches for part 2
sum = 0				# initializing variable to hold sum of real IDs
matches = []		# initializing matrix to hold indices of real rooms
for i in range(0, np.size(name_unique)):
	if name_unique[i] == checksum[i]:
		sum += id[i]
		matches.append(i)
print 'Sum of IDs: ' + str(sum)

#############################################################
# RESET AND REPARSE INPUT 

# with open('advent_04_test2.txt') as f:		# comment this line to run with actual data
with open('advent_04.txt') as f:				# comment this line to run test
	input = f.readlines()

# Remove \n from the end each line (except the last)
for i in range(0,np.size(input)-1):
	input[i] = input[i][0:-1]

# parse everything else
presum = []
id = []
name = presum
checksum = input
for i in range(0, np.size(input)):
	curLine = input[i]
	locBracket = curLine.find('[')
	presum.append(curLine[0:locBracket])
	id.append(int(presum[i][-3:len(presum[i])]))
	name[i] = name[i][0:-4]
	locBracket = input[i].find('[')
	checksum[i] = input[i][locBracket+1:-1]

#############################################################
# CRACK SHIFT CIPHER

# define alphabet sring that will be the key to the shift cipher
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(0, np.size(input)):
	nameList = list(name[i])
	for j in range(0,len(nameList)):
		if nameList[j] == '-':
			nameList[j] = ' '
		else:
			index = alphabet.find(nameList[j])
			index = (index + id[i]) % 26
			nameList[j] = alphabet[index]
	name[i] = "".join(nameList)
	if name[i] == 'northpole object storage':
		print 'Sector ID of "northpole object storage": ' + str(id[i])