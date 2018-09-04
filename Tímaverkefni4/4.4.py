n = int(input("Input an int: ")) # Do not change this line

teljari = 1
while teljari <= n:
    if n % teljari == 0:
        print(teljari)
    teljari += 1