import random
import string

def get_word_string(file):
    a_string = ""
    try:
        with open(file) as f:
            for line in f:
                a_string += line
        return a_string
    except:
        print("File {} not found".format(file))
        return a_string

def a_scramble(s_list):
    random.shuffle(s_list)
    scramble = "".join(s_list)
    return scramble

def scramble_word(word):
    if word[len(word)-1].isalnum():
        scramble_list = list(word[1:len(word)-1])
        scrambled = a_scramble(scramble_list)
        scrambled_word = word[0] + scrambled + word[len(word)-1:]
    else:
        scramble_list = list(word[1:len(word)-2])
        scrambled = a_scramble(scramble_list)
        scrambled_word = word[0] + scrambled + word[len(word)-2:]
    return scrambled_word

def scramble_string(string):
    new_string = string.strip("\n")
    a_list = new_string.split()
    for index, word in enumerate(a_list):
        if len(word) > 3:
            scrambled_word = scramble_word(word)
            a_list[index] = scrambled_word
    final_string = " ".join(a_list)
    return final_string

# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)