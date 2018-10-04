def merge_lists(list1, list2):
    a_list = [i for i in (list1 + list2)]
    new_list = []
    for item in a_list:
        if item not in new_list:
            new_list.append(item)
    new_list.sort()
    return new_list
    

# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
