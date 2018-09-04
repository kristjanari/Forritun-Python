m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line
max = 0

if m >= n:
    max = m
else:
    max = n
gcd = 0
for i in range(1,max+1):
    if m%i == 0 and n%i == 0:
        gcd = i
print(gcd)