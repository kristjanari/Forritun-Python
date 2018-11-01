s = input("Input a string: ")
buffer = ""
for letter in s:
    if letter.isdigit():
        buffer += letter

print(buffer)