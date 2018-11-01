def get_name():
    name = input("Enter name: ")
    name = name.lower()
    return name.split()
    
def common_letters_list(first,last):
    common = []
    for letter in first:
        if letter in last and letter not in common:
            common.append(letter)
    return common

def common_letters_set(first,last):
    return set(first) & set(last)

def main():
    first, last = get_name()
    common_letters = common_letters_list(first,last)

    print(sorted(common_letters))
    print(sorted(list(common_letters_set(first,last))))

main()