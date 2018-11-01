low = int(input("Input the lower bound: "))
high = int(input("Input the higher bound: "))
sum_of_odd = 0

for number in range(low, high + 1) :
    if number % 2 == 1 :
        sum_of_odd += number
    
print("Sum is", sum_of_odd)