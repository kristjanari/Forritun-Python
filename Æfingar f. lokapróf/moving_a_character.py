LEFT_LIMIT = 1
RIGHT_LIMIT = 10

def get_initial_position():
    return int(input("Input a position between 1 and 10: "))

def print_info():
    print(
"""l - for moving left
r - for moving right
Any other letter for quitting""")

def get_choice():
    return input("Input your choice: ")

def move(choice, position):
    if choice.lower() == "r":
        if position < RIGHT_LIMIT:
            return position + 1
    elif choice.lower() == "l":
        if position > LEFT_LIMIT:
            return position - 1
    return position

def main():
    position = get_initial_position()
    choice = "r"
    while choice.lower() in {"r", "l"}:
        print_info()
        choice = get_choice()
        position = move(choice, position)
        print("New position is :", position)

main()