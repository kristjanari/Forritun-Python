def information():
    print("""l - for moving left
r - for moving right
Any other letter for quitting""")
    
def move(staða):
    færsla = input("Input your choice: ")
    if (staða == 1 and færsla == "l") or (staða == 10 and færsla =="r"):
        return staða
    if færsla == "r":
        staða += 1
    elif færsla == "l":
        staða -= 1
    else:
        staða = 0
    return staða

Vinsri_endi = 1
Hægri_endi = 10
staðsetning = int(input("Input a position between 1 and 10: "))

while staðsetning != 0:
    information()
    staðsetning = move(staðsetning)
    print("New position is:", staðsetning)

