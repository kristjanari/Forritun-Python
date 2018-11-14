import random
import string

def get_word_string(filename):
    try:
        with open(filename) as f:
            file_string = f.read()
            return file_string.strip("\n")
    except:
        print("File '{}' not found".format(filename))

def scramble(word):
    letter_list = []
    for letter in word:
        letter_list.append(letter)
    random.shuffle(letter_list)
    word =  "".join(letter_list)
    return word

def scramble_word(word):
    if word[len(word)-1] in string.punctuation:
        word = word[0] + scramble(word[1:len(word)-2]) + word[len(word)-2:]
    else:
        word = word[0] + scramble(word[1:len(word)-1])+ word[len(word)-1:]
    return word

def scramble_string(word_string):
    word_list = word_string.split()
    for index, word in enumerate(word_list):
        if len(word) > 3:
            word_list[index] = scramble_word(word)
    return " ".join(word_list)
            

# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)