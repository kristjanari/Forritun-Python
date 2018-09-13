sum = 0
low = int(input("Sláðu inn neðri mörk bils: "))
high = int(input("Sláðu inn efri mörk bils: "))

for i in range (low,(high+1)):
    sum += i

print(sum)
