import hashlib as h

# returns the md5 hash of input string
def hashmd5(string):
	return h.md5(string).hexdigest()

# returns true if the input string begins with '00000'
def beginsWith5Zeros(string):
	if string[0:5] == "00000":
		return True
	else:
		return False

# returns true if the 6th character of the input string is in the range 0-7
def hasPlace(string):
	if string[5] == '0' or string[5] == '1' or string[5] == '2' or string[5] == '3' or string[5] == '4' or string[5] == '5' or string[5] == '6' or string[5] == '7':
		return True
	else:
		return False