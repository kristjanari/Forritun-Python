def get_list():
    my_list = []
    size = int(input("Enter the size of your list: "))
    for i in range(size):
        my_list.append(int(input("Input your value: ")))
    return my_list

def the_sum(a_list):
    return sum(a_list)

print(the_sum(get_list()))