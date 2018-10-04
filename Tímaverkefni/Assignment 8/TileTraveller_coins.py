# Það var betra að gera þetta forrit með föllum heldur en án falla.
# Okkur fannst umtalsvert einfaldara að ákvarða í hvaða átt
# mætti ferðast hverju sinni með föllum.
# Sérstaklega fannst okkur lesanlegra hvernig við ákvörðuðum strenginn "(N)orth or (E)ast or..."
# Það voru engin vandamál sem okkur tókst að leysa með föllum sem við gátum ekki leyst án falla, 
# en þetta hefði verið einfaldara ef við hefðum leyst þetta strax með föllum.
# Github repo: https://github.com/kristjanari/TileTraveller
x,y = 1,1
coin_count = 0

def north(x,y):
    if y == 3 or (x,y) == (2,2) or (x,y) == (3,1):
        return False
    return True

def east(x,y):
    if (x,y) != (1,2) and (x,y) != (1,3) and (x,y) != (2,3):
        return False
    return True

def west(x,y):
    if y == 1 or x == 1 or (x,y) == (3,2):
        return False
    return True

def south(x,y):
    if y == 1 or (x,y) == (2,3):
        return False
    return True

def string(n,e,s,w):
    dir = ""
    while dir == "":
        if n == True:
            dir += "(N)orth"
        elif e == True:
            dir += "(E)ast"
        elif s == True:
            dir += "(S)outh"
        elif w == True:
            dir += "(W)est"
    if e == True and dir != "(E)ast":
        dir += " or (E)ast"
    if s == True and dir != "(S)outh":
        dir += " or (S)outh"
    if w == True and dir != "(W)est":
        dir += " or (W)est"
    return dir
    
def command_call():
    i = input("Direction: ")
    i = i.upper()
    return i

def translocator(boolean):
    if boolean == True:
        return 1
    return 0

def move(x,y,string):
    if string == "N":
        y += translocator(N)
    elif string == "S":
        y -= translocator(S)
    elif string == "W":
        x -= translocator(W)
    elif string == "E":
        x += translocator(E)
    return x,y
    
def coins(quantity):
    question = input("Pull a lever (y/n): ")
    if question.lower() == "y":
        quantity += 1
        print("You received 1 coins, your total is now {}.".format(quantity))
    return quantity
while (x,y) != (3,1):
    a = x
    b = y
    N,E,S,W = True,True,True,True
    N = north(x,y)
    E = east(x,y)
    S = south(x,y)
    W = west(x,y)
    directions = string(N,E,S,W)
    print("You can travel: " + directions + ".")
    command = ""
    while (x,y) == (a,b):
        command = command_call()
        x,y = move(x,y,command)
        if (x,y) == (a,b):
            print("Not a valid direction!")
    if (x,y) in [(1,2),(2,2),(2,3),(3,2)]:
        coin_count = coins(coin_count)
print("Victory!")