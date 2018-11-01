turns = int(input("Hversu margar tölur viltu slá inn? "))

for i in range(turns):
    n = int(input("Veldu tölu: "))
    if n%2 == 1:
        print("you picked", n)