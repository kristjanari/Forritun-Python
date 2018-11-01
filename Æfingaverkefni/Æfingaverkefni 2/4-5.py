def get_list():
    my_list = []
    size = int(input("Enter the size of your list: "))
    for i in range(size):
        my_list.append(int(input("Input your value: ")))
    return my_list

def the_max(a_list):
    return max(a_list)

def the_min(a_list):
    return min(a_list)

print(the_max(get_list()))
print(the_min(get_list()))