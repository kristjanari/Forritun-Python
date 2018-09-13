n = int(input("Input an int: ")) # Do not change this line
sum = 0
for i in range(1,n+1):
    for j in range(0,i+1):
        sum += j
    print(sum)
    sum = 0
