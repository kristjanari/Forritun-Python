turns = int(input("Input the number of turns: "))

counter = 0

while counter < turns :
    choice = int(input("input a number: "))
    if choice % 2 == 1 :
      print("You picked", choice)
    counter += 1
