low = int(input("Input the lower bound: "))
high = int(input("Input the higher bound: "))

total_sum = 0

while low <= high :
    if low % 3 == 0 :
        total_sum += low
    low += 1

print("The sum is ", total_sum)