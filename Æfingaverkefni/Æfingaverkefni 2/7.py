def get_list():
    my_list = []
    size = int(input("Enter the size of your list: "))
    for i in range(size):
        my_list.append(int(input("Input your value: ")))
    return my_list

def no_dublicates(a_list):
    new_list = []
    for value in a_list:
        if value not in new_list:
            new_list.append(value)
    return new_list
    
my_list = get_list()
print(my_list)
print(no_dublicates(my_list))