import numpy as np

class Screen(object):

	# Magic function
	def __init__(self, numRows=6, numCols=50):
		self.numRows = numRows
		self.numCols = numCols
		self.screen = np.zeros((self.numRows, self.numCols), dtype=np.int8)

	# Returns the number of rows of the screen
	def getNumRows(self):
		return self.numRows

	# Returns the number of columns of the screen
	def getNumCols(self):
		return self.numCols

	# Returns the number of pixels in the screen
	def getSize(self):
		return np.size(self.screen)

	# Returns the number of rows and the number of columns of the screen
	def getShape(self):
		return np.shape(self.screen)

	# Returns the matrix of on/off values for the screen
	def getScreen(self):
		return self.screen

	# Prints the screen to the output window
	def show(self, on='#', off=' '):
		screen_string = ""
		for line in range(0, len(self.screen)):
			curLine = []
			for pixel in range(0, len(self.screen[line])):
				if self.screen[line][pixel] == 0:
					curLine.append(off)
				else:
					curLine.append(on)
			screen_string = screen_string + "".join(curLine) + '\n'
		# screen_string = screen_string[:-1]
		print screen_string

	# Returns the number of pixels turned on
	def getNumOn(self):
		numOn = 0
		for line in range(0, len(self.screen)):
			for pixel in range(0, len(self.screen[line])):
				if self.screen[line][pixel] == 1:
					numOn += 1
		return numOn

	# Turn on a rectangle of pixels in the top left corner of the screen with the given shape
	def rect(self, rRows, rCols):
		for line in range(0,rRows):
			self.screen[line][0:rCols] = 1

	# Shift the given row to the right by the given number of pixels
	def shiftR(self, row, num):
		self.screen[row] = np.roll(self.screen[row], num)

	# Shift the given row to the left by the given number of pixels
	def shiftL(self, row, num):
		self.screen[row] = np.roll(self.screen[row], -1 * num)

	# Shift the given column up by the given number of pixels
	def shiftU(self, col, num):
		self.screen[:,col] = np.roll(self.screen[:,col], -1 * num)

	# Shift the given column down by the given number of pixels
	def shiftD(self, col, num):
		self.screen[:,col] = np.roll(self.screen[:,col], num)

	# Shift the row/col by the given number of pixels along the given axis
	# axis=0 is the x-axis, axis=1 is the y-axis
	def shift(self, axis, row, num):
		if axis == 0:
			self.shiftR(row, num)
		if axis == 1:
			self.shiftD(row, num)