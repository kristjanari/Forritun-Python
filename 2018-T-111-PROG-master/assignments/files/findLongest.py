# This program finds the longest lower case word from an input file

file = open('words.txt', 'r')
maxLength = 0		# The length of the longest word found so far
longestWord = "" 	# The longest word found so far

for word in file:	# process each line/word
    word = word.strip() # strip leading and trailing white space
    length = len(word)	
    if length > maxLength:	 # A new maximum length?
        longestWord = word
        maxLength = length
print("Longest word is '{:s}' of length {:d}".format(longestWord, maxLength))
file.close