name = input("Input a name: ")

last, first = name.split()
#Fjarlægja kommu
last = last[:len(last)-1]
fyrsti = first[0]
strengur = fyrsti.upper() + "." + " " + last[0].upper() + last[1:]
print(strengur)