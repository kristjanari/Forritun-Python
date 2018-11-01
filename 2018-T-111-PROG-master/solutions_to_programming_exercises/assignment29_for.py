turns = int(input("Input the number of turns: "))

number_of_negatives = 0
sum_of_negatives = 0
number_of_positives = 0
sum_of_positives = 0

for number in range(turns) :
    choice = int(input("input a number: "))
    if choice < 1 :
        number_of_negatives += 1
        sum_of_negatives += choice
    else :
        number_of_positives += 1
        sum_of_positives += choice

print("You picked", number_of_negatives, "negative integers")
print("You picked", number_of_positives, "positive integers")
print("The sum of negatives:", sum_of_negatives)
print("The sum of positives:", sum_of_positives)