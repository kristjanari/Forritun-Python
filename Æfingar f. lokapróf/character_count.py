import string

def get_sentence():
    return input("Enter a sentence: ")

def count(sentence, count_dict):
    for item in sentence:
        if item.isupper():
            count_dict["Upper"] += 1
        elif item.islower():
            count_dict["Lower"] += 1
        elif item.isdigit():
            count_dict["Digits"] += 1
        elif item in string.punctuation:
            count_dict["Punc"] += 1

def print_messege(count_dict):
    print("{:>15}{:>5}".format("Upper case", count_dict["Upper"]))
    print("{:>15}{:>5}".format("Lower case", count_dict["Lower"]))
    print("{:>15}{:>5}".format("Digits", count_dict["Digits"]))
    print("{:>15}{:>5}".format("Punctuation", count_dict["Punc"]))

def main():
    sentence = get_sentence()
    count_dict = {"Upper": 0, "Lower": 0, "Digits": 0, "Punc": 0}
    count(sentence, count_dict)
    print_messege(count_dict)

main()