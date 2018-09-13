# is_prime function definition goes here
def is_prime(x):
    
    for i in range(2,x):
        if x ==2:
            return False
        elif x % i == 0:
            return False
    return True

num = int(input("Input an integer greater than 1: "))
# Call the function here and print out the appropriate message
if is_prime(num):
    print(num, "is a prime")
if is_prime(num) == False:
    print(num, "is not a prime")