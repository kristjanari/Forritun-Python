a = int(input("Sláðu inn tvær heiltölur til þess að vinna með, a = "))
b = int(input("b = "))
n = int(input("Veldu 1 til að leggja tölurnar saman, 2 til að draga b frá a eða 3 til þess að margfalda tölurnar saman: "))

if n == 1:
    print(a+b)
elif n==2:
    print(a-b)
elif n == 3:
    print(a*b)
else:
    print("invalid input")
