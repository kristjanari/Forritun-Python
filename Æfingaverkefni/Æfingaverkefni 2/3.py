def count(a_list,target):
    count = 0
    for value in a_list:
        if target == value:
            count += 1
    return count

def get_list():
    my_list = []
    size = int(input("Enter the size of your list: "))
    for i in range(size):
        my_list.append(int(input("Input your value: ")))
    return my_list

target = int(input("Input your target: "))
print(count(get_list(),target))
