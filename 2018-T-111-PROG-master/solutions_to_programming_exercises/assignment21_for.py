turns = int(input("Input the number of turns: "))

for number in range(turns) :
    choice = int(input("input a number: "))
    if choice % 2 == 1 :
        print("You picked", choice)
