def target_list(a_list,target):
    for value in a_list:
        if target == value:
            return True
    return False


my_list = []
size = int(input("Enter the size of your list: "))
for i in range(size):
    my_list.append(int(input("Input your value: ")))
target = int(input("Input your target: "))
if target_list(my_list,target):
    print("{} is in the list".format(target))
else:
    print("{} is not in the list".format(target))