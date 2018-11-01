with open('words.txt','r') as word_file:
    with open('sentences.txt','w') as sent_file:
        sentence = ''
        for word in word_file:	# process each line/word
            word = word.strip() # strip leading and trailing white space
            if word == '':  # sentence boundary
                sent_file.write(sentence+"\n")
                print(sentence)
                sentence = ''
            else:
                sentence = sentence + word + ' '