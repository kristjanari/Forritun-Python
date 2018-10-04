#game_of_eights() function goes here
def game_of_eights(listi):
    try:
        for index, value in enumerate(listi):
            if listi[index+1] == value and value == "8":
                return True
    except:
        return False

def main():
    spila = True
    a_list = input("Enter elements of list separated by commas: ").split(',')
    # remainder of main() goes here
    try:
        for value in a_list:
            int(value)
    except:
        print("Error. Please enter only integers.")
        spila = False
    if spila:
        print(game_of_eights(a_list))
main()