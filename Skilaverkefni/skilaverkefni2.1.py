setning = input("Enter a sentence:")

storir_stafir = 0
litlir_stafir = 0
tölur = 0
punktar = 0

for stafur in setning:
    if stafur.isupper():
        storir_stafir += 1
    if stafur.islower():
        litlir_stafir += 1
    if stafur.isdigit():
        tölur +=1
    #if stafur.ispunctuation():????????????????
        #punktar +=1

print(("{:>15}"+ "{:>5}").format("Upper case", str(storir_stafir)))
print(("{:>15}"+ "{:>5}").format("Lower case", str(litlir_stafir)))
print(("{:>15}"+ "{:>5}").format("Digits", str(tölur)))
print(("{:>15}"+ "{:>5}").format("Punctuation", str(punktar)))