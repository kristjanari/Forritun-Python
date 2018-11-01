# Function definitions start here
def open_file(file):
    try:
        a_file = open(file)
        return a_file
    except:
        return None


def get_longest_word(file):
    a_string = file.read()
    a_list = a_string.split("\n")
    max_length = 0
    for word in a_list:
        if len(word) >= max_length:
            max_length = len(word)
            longest = word 
    return longest

# The main program starts here
filename = input("Enter name of file: ")
file_stream = open_file(filename)
if file_stream:
	longest_word = get_longest_word(file_stream)
	print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
	file_stream.close
else:
	print('File',filename,'not found!')

