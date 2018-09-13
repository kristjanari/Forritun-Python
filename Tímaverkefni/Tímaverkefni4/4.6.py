teljari = 10
tala = 0
while teljari**2 < 1000:
    if teljari == (teljari**2 % 100):
        tala = teljari
        break
    teljari += 1

print(tala)