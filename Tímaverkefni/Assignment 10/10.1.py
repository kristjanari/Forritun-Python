import string

sentence = input("Input a sentence: ")
# Here you should add the missing part
unique_letters = []

for value in sentence:
    if (value in unique_letters) == False:
        unique_letters.append(value)
for item in unique_letters:
    if item.isalpha() == False or item == " - ":
        unique_letters.remove(item)    

print("Unique letters:", unique_letters)