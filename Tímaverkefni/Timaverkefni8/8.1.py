def find_min(x, y):
    if x <= y:
        return x
    else:
        return y

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Minimum:", find_min(a, b))