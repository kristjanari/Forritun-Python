lán = float(input("Input the cost of the item in $: "))
vextir = 0.0
mánuður = 0
greiddirvextir = 0
afborgun = 0.0
heildarvextir = 0
if lán <= 1000.0:
    vextir = 0.015
else:
    vextir = 0.02
while lán > 0.0:
    greiddirvextir = lán*vextir
    lán += greiddirvextir
    if lán > 50.0:
        afborgun = 50.0
    else:
        afborgun = lán
    lán = lán - afborgun
    mánuður += 1
    heildarvextir += greiddirvextir
    print("Month:", mánuður, "Payment:", round(afborgun,2), "Interest paid:", round(greiddirvextir,2), "Remaining debt:", round(lán,2))

print()
print("Number of months:", mánuður)
print("Total interest paid:", round(heildarvextir,2))