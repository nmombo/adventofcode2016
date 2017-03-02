#############################################################
# READ INPUT FROM FILE

filename = 'advent_09_test1.txt'
filename = 'advent_09.txt'			# result > 14380
with open(filename) as file:
	input = file.readlines()
input = input[0]

#############################################################
# DECOMPRESS THE STRING

# Loop through the string for each character. Note that len(input) will be variable since input
# will be modified for certain char values (when a compression marker is found).
char = 0 # initialize variable to hold the location of the current operating character
while char < len(input):
	# Search for compression markers in the string. Compression markers have the form (123x456).
	# The above example would require that the next 123 numbers be repeated 456 times.
	if input[char] == "(":
		# Find the important indices for parsing a compression marker
		index_num1_start = char+1									# beginning of first number
		index_x = input[char:].find('x') + char 					# x of by
		index_num2_start = index_x+1 								# beginning of second number
		index_closeParen = input[char:].find(')') + char 			# close parenthesis
		# Find the key ints of the compression marker
		numCharsToRepeat = int(input[index_num1_start:index_x])
		numTimesToRepeat = int(input[index_num2_start:index_closeParen])
		# Print a debugging message about proper identification of the key numbers of compression markers
		print 'char: ' + str(char) + '\n  numCharsToRepeat: ' + str(numCharsToRepeat) + '\n  numTimesToRepeat: ' + str(numTimesToRepeat)
		# Find the characters that need to be repeated
		charsToRepeat = input[index_closeParen+1:index_closeParen+numCharsToRepeat+1]
		print '  charsToRepeat:    ' + charsToRepeat
		# Repeat the characters
		stringToInsert = charsToRepeat
		for rep in range(0, numTimesToRepeat-1):
			stringToInsert += charsToRepeat
		# Remove the compression marker
		input = input[:char] + input[index_closeParen+1:]
		# Insert the repeated characters into the string
		input = input[:char] + stringToInsert + input[char+len(stringToInsert):]
		# Print the results of this iteration of the loop for debugging
		print '  ' + input[char:char+len(stringToInsert)+3]
		# Iterate by skipping to the end of the inserted string
		char += numCharsToRepeat * numTimesToRepeat
	else:
		print 'char: ' + str(char)
		char += 1
print len(input)