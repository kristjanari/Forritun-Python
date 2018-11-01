turns = int(input("Input the number of turns: "))

counter = 0
number_of_negatives = 0
number_of_positives = 0

while counter < turns :
    choice = int(input("input a number: "))
    if choice < 0 :
        number_of_negatives += 1
    else :
        number_of_positives += 1
    counter += 1
print("You picked", number_of_negatives, "negative integers")
print("You picked", number_of_positives, "positive integers")