# numInstances returns the number of instances of letter in string
def numInstances(string, letter):
	count = 0
	for i in range(0,len(string)):
		if string[i] == letter:
			count += 1
	return count

# removeDupliChar removes duplicate characters from string
def removeDupliChar(string):
	newString = ""
	for i in range(0,len(string)):
		if string[i] not in newString:
			newString = newString + string[i]
	return newString