#############################################################
# IMPORT LIBRARIES
import numpy as np
from advent_05_functions import *

#############################################################
# RECIEVE INPUT
input = 'abc'				# test case, expected output '18f47a30'
input = 'cxdnnyjw'

#############################################################
# PART 1
index = 0 		# counter for the index
indices = []	# list of indices that workthat work
password = ""
while np.size(indices) < 8: # while the password is incomplete in length 
	digit =  np.size(indices)	# tells the current digit being found
	curHash = hashmd5(input + str(index))	# store the hash of the current index
	if beginsWith5Zeros(curHash):					# if we have a 00000 match:
		indices.append(index)						# add the index to the list of indices
		password = password + str(curHash[5])		# add the correct digit of the hash to the password
		print 'index ' + str(index) + ', password ' + str(password)
	index += 1
print "done"