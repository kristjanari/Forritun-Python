low = int(input("Input the lower bound: "))
high = int(input("Input the higher bound: "))

total_sum = 0

while low <= high :
    total_sum += low
    low += 1

print("The sum is ", total_sum)