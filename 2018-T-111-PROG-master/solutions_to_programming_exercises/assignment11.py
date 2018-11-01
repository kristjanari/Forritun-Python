a = int(input("Please input an integer: "))
b = int(input("Please input another integer: "))
choice = int(input("Please input your choice: "))

if choice == 1 :
    print(a + b)
elif choice == 2 :
    print(a - b)
elif choice == 3 :
    print(a * b)
else :
    print("Invalid input")