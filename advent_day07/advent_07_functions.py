# Returns true if the input string follows Autonomous Bridge Bypass Annotation (ABBA).
# ABBA is a pair of two different characters followed by the reverse of that pair.
def checkABBA(string):
	# return false if the string is too short to follow ABBA
	if len(string) < 4:
		return False
	# if the string contains brackets, remove them. recheck for length
	if string[0] == '[':
		string = string[1:-1]
		if len(string) < 4:
			return False
	# for each two-letter pair before the end pair
	# check to see if this pair is the reverse of the next pair and
	# check to see if this pair has two different letters
	for i in range(0, len(string)-3):
		thisPair = string[i:i+2]
		nextPair = string[i+2:i+4]
		if thisPair[0] != thisPair[1] and thisPair == nextPair[::-1]:
			return True
	# return false if the string didn't contain the ABBA sequency anywhere
	return False


# Returns a list of ABA-following strings that are contained in the input string.
# Area-Broadcast Accessor (ABA) is a series of two characters followed by the first character.
def findABA(string):
	# return empty if the string is too short to follow ABA
	if len(string) < 3:
		return []
	# the string should not contain brackets, so if it does, return empty
	if string[0] == '[':
		return []
	# check each two-letter pair before the end letter
	# check to see if the next letter is the first letter in this pair and
	# check to see if this pair has two different letters
	listABA = []
	for i in range(0, len(string)-2):
		thisPair = string[i:i+2]
		nextLet = string[i+2]
		if thisPair[0] != thisPair[1] and thisPair[0] == nextLet:
			listABA.append(string[i:i+3])
	return listABA


# Returns true if the input string follows BAB according to the given ABA.
# Area-Broadcast Accessor (ABA) is a series of two characters followed by the first character.
# Byte Allocation Block (BAB) is the opposite of Area-Broadcast Accessor (ABA).
def checkBAB(string, ABA):
	# return false if the input string is too short to follow BAB
	if len(string) < 3:
		return False
	# if the string contains brackets (which it should), remove them. recheck for length
	if string[0] == '[':
		string = string[1:-1]
		if len(string) < 3:
			return False
	# find BAB for comparison to string by reversing ABA
	BAB = ABA[1] + ABA[0] + ABA[1]
	# check each three-letter string to see if this string matches BAB
	for i in range(0, len(string)-2):
		thisThree = string[i:i+3]
		if thisThree == BAB:
			return True
	# return False if none of the three-letter strings matched BAB
	return False