def get_input():
    return input("Name: "), input("Number: ")

def add_contact(a_dict,name,number):
    a_dict[name] = number

def dict_to_tuple(a_dict):
    tuple_list = []
    for key, value in a_dict.items():
        tuple_list.append((key, value))
    return tuple_list

def main():
    choice = "y"
    phone_book = {}
    while choice.lower() == "y":
        name, number = get_input()
        add_contact(phone_book, name, number)
        choice = input("More data (y/n)? ")
        phone_book_list = dict_to_tuple(phone_book)
    print(sorted(phone_book_list))

main()