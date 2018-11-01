low = int(input("Input the lower bound: "))
high = int(input("Input the higher bound: "))
total_sum = 0

for number in range(low, high + 1) :
    if number % 3 == 0 or number % 5 == 0:
        total_sum += number
    
print("Sum is", total_sum)