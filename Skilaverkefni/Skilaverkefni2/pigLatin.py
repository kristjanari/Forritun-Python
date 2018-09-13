orð = "a"

sérhljóðar = "aeiou"
byrjar_á_sérhljóða = False
fyrsti_fundinn = False
fyrsti_sérhljóði = 0
while orð != ".":
    orð = input("Enter a word: ")
    if orð == ".":
        break
    for stafur in sérhljóðar:
        if orð[0] == stafur:
            byrjar_á_sérhljóða = True
    if byrjar_á_sérhljóða:
        orð += "yay"
        byrjar_á_sérhljóða = False
    else:
        for sæti,stafur in enumerate(orð):
            for stafur2 in sérhljóðar:
                if stafur == stafur2:
                    fyrsti_sérhljóði = sæti
                    fyrsti_fundinn = True
            if fyrsti_fundinn:
                break        
        fyrsti_fundinn = False
        orð = orð[fyrsti_sérhljóði:] + orð[:fyrsti_sérhljóði] + "ay"
        fyrsti_sérhljóði = 0
    
    print(orð)

    
            
