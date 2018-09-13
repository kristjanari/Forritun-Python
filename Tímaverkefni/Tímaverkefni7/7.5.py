s = input("Input a string: ")

strengur = ""
for sæti,stafur in enumerate(s):
    if stafur.isdigit():
        strengur += s[sæti]

print(strengur)
