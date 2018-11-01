import string

sentence = input("Input a sentence: ")

unique_letters = []
for c in sentence:
	if c not in string.punctuation and c not in string.whitespace and c not in unique_letters:
		unique_letters.append(c)
print("Unique letters:", unique_letters)
