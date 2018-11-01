from string import punctuation

def find_unique(wordlist):
    unique = []
    
    for word in wordlist:
        if word not in unique:
            unique.append(word)
    return unique
    
def build_wordlist(filestream):
    word_list = []
    
    for line in filestream:
        wordlist = line.strip(punctuation).split()
        for words in wordlist:
            word_list.append(words)
    return word_list
        
def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)  
    infile.close()  
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()