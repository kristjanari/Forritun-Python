def get_word():
    return input("Enter a word: ")

def scramble_word(word):
    vowels = {"a","e","i","o","u"}
    if word[0] in vowels:
        return word + "yay"
    else: 
        for letter in word:
            if letter not in vowels:
                word = word[1:] + word[0]
            else:
                return word + "ay"
        



def main():
    word = ""
    while word != ".":
        word = get_word()
        print(scramble_word(word))

main()