#############################################################
# IMPORT LIBRARIES
import numpy as np
from advent_05_functions import *

#############################################################
# RECIEVE INPUT
input = 'abc'				# test case, expected output '05ace8e3'
input = 'cxdnnyjw'

#############################################################
# PART 2
index = 0 		# counter for the index
digits = []		# list of digits that have been filled
password = ["_","_","_","_","_","_","_","_"]
while np.size(digits) < 8: # while the password is incomplete in length 
	curHash = hashmd5(input + str(index))	# store the hash of the current index
	if beginsWith5Zeros(curHash) and hasPlace(curHash) and curHash[5] not in digits:	# if we have a 00000 match AND the 7th place matches AND we have not already filled the found digit:
		digits.append(curHash[5])						# add the index to the list of indices
		password[int(curHash[5])] = str(curHash[6])		# add the correct digit of the hash to the password
		print 'index ' + str(index) + ', password ' + "".join(password)
	index += 1
print "done"