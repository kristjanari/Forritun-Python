hola = 1

while hola <= 18:
    par = int(input("Par of hole " + str(hola) + ": "))
    högg = int(input("Score on hole " + str(hola) + ": "))
    if högg + 3 < par:
        print("invalid score")
    elif högg + 3 == par:
        print("albatross")
    elif högg + 2 == par:
        print("eagle")
    elif högg + 1 == par:
        print("birdie")
    elif högg == par:
        print("par")
    elif högg - 1 == par:
        print("bogey")
    elif högg - 2 == par:
        print("double bogey")
    elif högg - 3 == par:
        print("triple bogey")
    elif högg - 3 > par:
        print("bad hole")
    hola +=1