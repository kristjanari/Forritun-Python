def open_file(filename):
	''' Opens the given filename for reading.
		Returns a reference to the file stream, if successful, otherwise None
	'''
	try:
		file_stream = open(filename, 'r')
		return file_stream
	except FileNotFoundError:
		return None

def get_longest_word(file_stream):
	''' Returns the longest word in a file_stream, consisting of one word/token per line '''
	longest_word = ''
	maxLength = 0
	for word in file_stream:	# process each line/word
		word = word.strip() # strip leading and trailing white space
		length = len(word)	
		if length > maxLength:	 # A new maximum length?
			longest_word = word
			maxLength = length
	return longest_word

# The main program starts here
filename = input("Enter name of file: ")
file_stream = open_file(filename)
if file_stream:
	longest_word = get_longest_word(file_stream)
	print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
	file_stream.close()
else:
	print('File',filename,'not found!')
