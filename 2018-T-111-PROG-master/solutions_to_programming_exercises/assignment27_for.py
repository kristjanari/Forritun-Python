turns = int(input("Input the number of turns: "))

number_of_negatives = 0

for number in range(turns) :
    choice = int(input("input a number: "))
    if choice < 1 :
        number_of_negatives += 1

print("number of negative numbers:", number_of_negatives)
