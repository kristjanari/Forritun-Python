
def get_sets():
    list_1 = input("Input a list of integers separated with a comma: ").split(",")
    list_2 = input("Input a list of integers separated with a comma: ").split(",")
    int_list_1 = [int(i) for i in list_1]
    int_list_2 = [int(i) for i in list_2]
    return set(int_list_1), set(int_list_2)

def print_instructions():
    print(
"""1. Intersection
2. Union
3. Difference
4. Quit""")

def loop(set_1,set_2):
    choice = "1"
    while choice in {"1","2","3"}:
        print_instructions()
        choice = input("Set operation: ")
        if choice == "1":
            print(set_1 & set_2)
        elif choice == "2":
            print(set_1 | set_2)
        elif choice == "3":
            print(set_1 - set_2)


def main():
    set_1, set_2 = get_sets()
    print(set_1)
    print(set_2)
    loop(set_1,set_2)
    
main()