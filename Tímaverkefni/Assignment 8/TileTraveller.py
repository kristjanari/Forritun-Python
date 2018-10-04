# Við skilgreinum x = 1 og y = 1
# Við skilgreinum allar áttirnar og gerum lista yfir hvenær þú mátt fara upp,
# hvenær má fara niður og hvenær má fara til vinstri eða hægri
# Þá látum við N = True eða N = False eftir því hvort þú getur farið upp eða ekki, gerum þetta fyrir allar áttirnar
# Látum forritið enda þegar x = 3 og y = 1
# Github repo: https://github.com/kristjanari/TileTraveller
x,y = 1,1








while (x,y) != (3,1):
    a = x
    b = y
    N = True
    E = True
    S = True
    W = True
    if y == 3 or (x,y) == (2,2) or (x,y) == (3,1):
        N = False
    if (x,y) != (1,2) and (x,y) != (1,3) and (x,y) != (2,3):
        E = False
    if y == 1 or (x,y) == (2,3):
        S = False
    if y == 1 or x == 1 or (x,y) == (3,2):
        W = False
    directions = ""
    while directions == "":
        if N == True:
            directions += "(N)orth"
        elif E == True:
            directions += "(E)ast"
        elif S == True:
            directions += "(S)outh"
        elif W == True:
            directions += "(W)est"
    if E == True and directions != "(E)ast":
        directions += " or (E)ast"
    if S == True and directions != "(S)outh":
        directions += " or (S)outh"
    if W == True and directions != "(W)est":
        directions += " or (W)est"
    print("You can travel: " + directions + ".")
    command = ""
    while (x,y) == (a,b):
        command = input("Direction: ")
        command = command.upper()
        if command == "N" and N == True:
            y += 1
        elif command == "S" and S == True:
            y -= 1
        elif command == "W" and W == True:
            x -= 1
        elif command == "E" and E == True:
            x += 1
        else:
            print("Not a valid direction!")
print("Victory!")