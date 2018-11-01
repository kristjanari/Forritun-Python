def add_to_dict(a_dict, a_key,a_value):
    if a_key not in a_dict:
        a_dict[a_key] = a_value
    else:
        print("Error. Key already exists.")

def remove_from_dict(a_dict,a_key):
    try:
        a_dict.pop(a_key)
    except:
        print("No such key exists in the dictionary.")

def find_key(a_dict,a_key):
    try:
        print("Value:",a_dict[a_key])
    except:
        print("Key not found.")

def menu_selection():
    print("Menu: ")
    choice = input("add(a), remove(r), find(f): ")
    return choice

def execute_selection(a_choice, a_dict):
    if a_choice == "a":
        a_key = input("Key: ")
        a_value = input("Value: ")
        add_to_dict(a_dict,a_key,a_value)
    elif a_choice == "r":
        remove_key = input("key to remove: ")
        remove_from_dict(a_dict,remove_key)
    elif a_choice == "f":
        find = input("Key to locate: ")
        find_key(a_dict,find)
    else:
        print("Invalid choice.")

def dict_to_tuples(a_dict):
    a_list = []
    for key,value in a_dict.items():
        a_list.append((key,value))                
    return a_list

# Do not change this main function
def main():
    more = True
    a_dict = {}
    
    while more:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more = again.lower() == 'y'
    
    dictlist = dict_to_tuples(a_dict)
    print(sorted(dictlist))

main()