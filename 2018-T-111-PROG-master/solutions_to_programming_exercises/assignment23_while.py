low = int(input("Input the lower bound: "))
high = int(input("Input the higher bound: "))

sum_of_odd = 0

while low <= high :
    if low % 2 == 1 :
        sum_of_odd += low
    low += 1

print("The sum is ", sum_of_odd)