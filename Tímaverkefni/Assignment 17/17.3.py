class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence

    def get_first_word(self):
        wordlist = self.get_all_words()
        return wordlist[0]

    def get_all_words(self):
        return self.sentence.split()

    def replace(self, index, new_word):
        try:
            wordlist = self.get_all_words()
            wordlist[index] = new_word
            new_sentence = " ".join(wordlist)
            self.sentence = new_sentence
        except:
            pass

sent = Sentence('Here we have a longer sentence')
print(sent.get_first_word())
print(sent.get_all_words())
sent.replace(2, "find")
print(sent.get_all_words())
sent.replace(10,"bla")
print(sent.get_all_words())
