my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code
kvóti = my_int
afgangur = 0
binary_öfugur = ""
while kvóti != 0:
    afgangur = 0
    if kvóti%2 != 0:
        afgangur = 1
    binary_öfugur += str(afgangur)
    kvóti = kvóti//2
if my_int == 0:
    bstr = 0
else:
    bstr = binary_öfugur[::-1]
print("The binary of", my_int, "is", bstr)