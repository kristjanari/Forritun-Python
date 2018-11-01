turns = int(input("Hversu margar tölur viltu slá inn? "))
teljari_n = 0
teljari_j = 0
for i in range(turns):
    n = int(input("Veldu tölu: "))
    if n < 0:
        teljari_n += 1
    elif n > 0:
        teljari_j += 1


print("Neikvæðar töur: ", teljari_n)
print("Jákvæðar töur: ", teljari_j)
