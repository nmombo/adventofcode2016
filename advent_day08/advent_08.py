#############################################################
# IMPORT LIBRARIES

from advent_08_screen import Screen

#############################################################
# READ INPUT FROM FILE

filename = 'advent_08_test1.txt'	# test case
filename = 'advent_08.txt'			# comment this line to run test case
with open(filename) as file:
	input = file.readlines()

#############################################################
# PARSE INPUT AND FOLLOW INSTRUCTIONS

# Remove /n from every line except the last
for line in range(0, len(input) - 1):
	input[line] = input[line][:-1]

s = Screen()
for line in range(0, len(input)):
	# If instruction is 'rect', create a rectangle
	if input[line][0:4] == 'rect':
		index_firstNum = input[line].find(' ') + 1
		index_x = input[line].find('x')
		firstNum = input[line][index_firstNum:index_x]
		secondNum = input[line][index_x+1:]
		s.rect(int(secondNum), int(firstNum))
	# If instruction is 'rotate'
	else:
		# shorten instruction to remove unecessary rotate and row/column
		input[line] = input[line][input[line].find(' ')+1:]
		input[line] = input[line][input[line].find(' ')+1:]
		# determine axis of rotation
		if input[line][0] == 'x':
			axis = 1
		else:
			axis = 0
		# determine row to shift
		index_equals = input[line].find('=')
		index_space = input[line].find(' ')
		row = int(input[line][index_equals+1:index_space])
		# determine amount to shift
		index_b = input[line].find('b')
		num = int(input[line][index_b+3:])
		# shift with parsed instructions
		s.shift(axis, row, num)
print str(s.getNumOn()) + ' pixels on\n'
s.show('#')
