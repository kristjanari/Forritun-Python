
tala_1 = int(input("Sláðu inn heiltölu: "))
min = tala_1
teljari = 0

while teljari < 2:
    tala = int(input("Sláðu inn heiltölu: "))
    if tala < min:
        min = tala 
    teljari += 1

print(min)