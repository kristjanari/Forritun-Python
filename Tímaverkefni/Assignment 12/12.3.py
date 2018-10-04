import string

#build_wordlist() function goes here
def build_wordlist(file):
    wordlist = file.read().split()
    for i in string.punctuation:
        for index, value in enumerate(wordlist):
            wordlist[index] = value.strip(i)
    return wordlist

#find_unique() function goes here
def find_unique(words):
    new_words = []
    for value in words:
        if value in new_words:
            continue
        else:
            new_words.append(value.lower())
    return new_words

def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)  
    infile.close()
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()
