my_int = int(input('Give me an int >= 0: '))

if my_int == 0:
    bstr = '0'
else:
    bstr = ''
    quotient = my_int
    while quotient > 0:
        bstr = str(quotient % 2) + bstr
        quotient = quotient // 2
print("The binary of", my_int, "is", bstr)