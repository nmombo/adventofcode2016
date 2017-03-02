#############################################################
# IMPORT NUMPY
import numpy as np

#############################################################
# RECEIVE INPUT CODE

# literal input from AoC++
code = np.array(['ULL', 'RRDDD', 'LURDL', 'UUUUD'], dtype=object) # expect 1985, 5DB3
code = np.array(['RRLUDDLDUDUDUDRDDDRDDRLUUUDRUDURURURLRDDULLLDRRRRULDDRDDURDLURLURRUULRURDDDDLDDRRLDUDUUDURURDLDRRURDLLLDLLRUDRLDDRUULLLLLRRLDUDLUUDRUULLRLLLRLUURDLDLLDDRULDLUURRURLUUURLLDDULRDULULRULDDLRDDUUDLRRURLLURURLDDLURRLUURRRRLDRDLDUDRUDDRULLDUDDLRRLUUUUUDDLLDRLURDDRLLUDULDRDDLLUURUUUURDRLRLLULUULULLRRDLULRUDURDLRLRDDDRULLUULRURULLLUDUURUUUURUULDURDRRRULRLULDLRRULULUUDDDRDURLLURLLDUUUUDULRDLRDUUDDLDUDRLLRLRRRLULUDDDURLRRURUDDDRDRDRLLRDRDLDDRRDRDLLRLLLRRULRDDURRDUDRURDLDULLRRLURLRLLDURRRLLDRRURRRUULDRLDUULRDLDLURUDLLDLLUUDDDUUUDRL',
				 'DLRRDRRDDRRDURLUDDDDDULDDLLDRLURDDDDDDRDDDRDDDLLRRULLLRUDULLDURULRRDLURURUDRUURDRLUURRUDRUULUURULULDDLLDDRLDUDDRDRDDUULDULDDLUDUDDUDLULLUDLLLLLRRRUURLUUUULRURULUDDULLLRLRDRUUULULRUUUULRDLLDLDRDRDRDRRUUURULDUUDLDRDRURRUDDRLDULDDRULRRRLRDDUUDRUDLDULDURRDUDDLULULLDULLLRRRDULLLRRURDUURULDRDURRURRRRDLDRRUDDLLLDRDRDRURLUURURRUUURRUDLDDULDRDRRURDLUULDDUUUURLRUULRUURLUUUDLUDRLURUDLDLDLURUURLDURDDDDRURULLULLDRDLLRRLDLRRRDURDULLLDLRLDR',
				 'URURLLDRDLULULRDRRDDUUUDDRDUURULLULDRLUDLRUDDDLDRRLURLURUUDRLDUULDRDURRLLUDLDURRRRLURLDDRULRLDULDDRRLURDDRLUDDULUDULRLDULDLDUDRLLDDRRRDULLDLRRLDRLURLUULDDDDURULLDLLLDRRLRRLLRDDRDLDRURRUURLLDDDLRRRRRDLRRDRLDDDLULULRLUURULURUUDRULRLLRDLDULDRLLLDLRRRUDURLUURRUDURLDDDRDRURURRLRRLDDRURULDRUURRLULDLUDUULDLUULUDURRDDRLLLRLRRLUUURRDRUULLLRUUURLLDDRDRULDULURRDRURLRRLRDURRURRDLDUDRURUULULDDUDUULDRDURRRDLURRLRLDUDRDULLURLRRUDLUDRRRULRURDUDDDURLRULRRUDUUDDLLLURLLRLLDRDUURDDLUDLURDRRDLLRLURRUURRLDUUUUDUD',
				 'DRRDRRRLDDLDUDRDLRUUDRDUDRRDUDRDURRDDRLLURUUDRLRDDULLUULRUUDDRLDLRULDLRLDUDULUULLLRDLURDRDURURDUDUDDDRRLRRLLRULLLLRDRDLRRDDDLULDLLUUULRDURRULDDUDDDURRDRDRDRULRRRDRUDLLDDDRULRRLUDRDLDLDDDLRLRLRLDULRLLRLRDUUULLRRDLLRDULURRLDUDDULDDRLUDLULLRLDUDLULRDURLRULLRRDRDDLUULUUUULDRLLDRDLUDURRLLDURLLDDLLUULLDURULULDLUUDLRURRRULUDRLDRDURLDUDDULRDRRDDRLRRDDRUDRURULDRRLUURUDULDDDLRRRRDRRRLLURUURLRLULUULLRLRDLRRLLUULLDURDLULURDLRUUDUUURURUURDDRLULUUULRDRDRUUDDDRDRL',
				 'RLRUDDUUDDDDRRLRUUDLLDRUUUDRRDLDRLRLLDRLUDDURDLDUDRRUURULLRRLUULLUDRDRUDDULRLLUDLULRLRRUUDLDLRDDDRDDDUDLULDLRRLUDUDDRRRRDRDRUUDDURLRDLLDLDLRRDURULDRLRRURULRDDLLLRULLRUUUDLDUURDUUDDRRRDDRLDDRULRRRDRRLUDDDRUURRDRRDURDRUDRRDLUDDURRLUDUDLLRUURLRLLLDDURUDLDRLRLLDLLULLDRULUURLDDULDDRDDDURULLDRDDLURRDDRRRLDLRLRRLLDLLLRDUDDULRLUDDUULUDLDDDULULDLRDDLDLLLDUUDLRRLRDRRUUUURLDLRRLDULURLDRDURDDRURLDLDULURRRLRUDLDURDLLUDULDDU'], dtype=object)

#############################################################
# DEFINE KEYPAD 1
keypad = [[1,2,3],
          [4,5,6],
          [7,8,9]]

#############################################################
# FIND DIGITS (on keyppad 1)
i = 0
digits = np.zeros(np.size(code))
while i < np.size(code):
	# set inital key to be 5
	curLoc = [1,1]
	# loop through all instructions
	j = 0
	while j < len(code[i]):
		# change location
		curMove = code[i][j]
		if curMove == 'U':
			curLoc[0] -= 1
		if curMove == 'D':
			curLoc[0] += 1
		if curMove == 'R':
			curLoc[1] += 1
		if curMove == 'L':
			curLoc[1] -= 1
		# check and correct extremities
		if curLoc[0] < 0:
			curLoc[0] = 0
		if curLoc[0] > 2:
			curLoc[0] = 2
		if curLoc[1] < 0:
			curLoc[1] = 0
		if curLoc[1] > 2:
			curLoc[1] = 2
		j += 1
	# set digit
	digits[i] = keypad[curLoc[0]][curLoc[1]]
	# increment
	i += 1
print digits

#############################################################
# DEFINE NEW KEYPAD
keypad = [[0 ,0 ,0 ,0 ,0 ,0 ,0],
		  [0 ,0 ,0 ,1 ,0 ,0 ,0],
          [0 ,0 ,2 ,3 ,4 ,0 ,0],
          [0 ,5 ,6 ,7 ,8 ,9 ,0],
          [0 ,0 ,10,11,12,0 ,0],
          [0 ,0 ,0 ,13,0 ,0 ,0],
          [0 ,0 ,0 ,0 ,0 ,0 ,0]] # A=10, B=11, C=12, D=13

#############################################################
# FIND DIGITS (on new kepad)
digits = np.zeros(np.size(code))			# initializing digits to store the final code
i = 0										# index to count the number of digits in the code
curLoc = np.array([3,1])					# initializing curLoc to store current location, beginning at 5 on the keypad
while i < np.size(code):
	j = 0					    			# index to count the number of moves for each digit
	while j < len(code[i]):
		curMove = code[i][j]
		okToMove = False
		# check for ability to move
		if curMove == 'U' and keypad[curLoc[0]-1][curLoc[1]] != 0:
			okToMove = True
		if curMove == 'D' and keypad[curLoc[0]+1][curLoc[1]] != 0:
			okToMove = True
		if curMove == 'R' and keypad[curLoc[0]][curLoc[1]+1] != 0:
			okToMove = True
		if curMove == 'L' and keypad[curLoc[0]][curLoc[1]-1] != 0:
			okToMove = True
		# move if possible
		if okToMove and curMove == 'U':
			curLoc[0] -= 1
		if okToMove and curMove == 'D':
			curLoc[0] += 1
		if okToMove and curMove == 'R':
			curLoc[1] += 1
		if okToMove and curMove == 'L':
			curLoc[1] -= 1
		# increment
		j += 1 
	digits[i] = keypad[curLoc[0]][curLoc[1]]
	i += 1

#############################################################
# CONVERT DIGITS TO STRING (for new keypad)
digits_string = np.array(['','','','',''], dtype=object)
i = 0
while i < np.size(code):
	if digits[i] == 10:
		digits_string[i] = 'A'
	elif digits[i] == 11:
		digits_string[i] = 'B'
	elif digits[i] == 12:
		digits_string[i] = 'C'
	elif digits[i] == 13:
		digits_string[i] = 'D'
	elif digits[i] == 0:
		digits_string[i] = 'WRONG'
	else:
		digits_string[i] = str(digits[i])[0]
	i += 1
print digits_string