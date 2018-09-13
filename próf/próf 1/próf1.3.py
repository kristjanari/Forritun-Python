upphafsgildi = int(input("Initial value: "))
mismunur = int(input("Step: "))
summa = 0
númer_staks = 0
strengur = ""

while summa < 100:
    stak = upphafsgildi+númer_staks*mismunur
    summa += stak
    strengur += (str(stak) + " ")
    númer_staks += 1

print(strengur)
print("Sum of series:", summa)
