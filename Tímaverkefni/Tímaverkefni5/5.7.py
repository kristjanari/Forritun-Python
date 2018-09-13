n = int(input("Input a number between 0 and 999: "))
for i in range(0,n):
    sum = 0
    strengur = str(i)
    for stafur in strengur:
        sum += 1
        seinnitveir = i%100
        tala1 = seinnitveir%10
        tala2 = seinnitveir//10
        tala3 = i//100
    if i == tala1**sum + tala2**sum + tala3**sum:
        print(i)    
