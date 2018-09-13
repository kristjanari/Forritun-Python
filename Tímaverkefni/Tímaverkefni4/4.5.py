import math
n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
teljari = 2
prime = True
while teljari < n:
    if n % teljari == 0:
        prime = False
        break
    teljari += 1

if prime:
    print("Prime")
else:
    print("!Prime")