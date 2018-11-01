a = int(input("Please input an integer: "))
b = int(input("Please input another integer: "))
c = int(input("Please input another integer: "))

min_value = a

if b < min_value :
    min_value = b
if c < min_value :
    min_value = c

print("The min value is", min_value)