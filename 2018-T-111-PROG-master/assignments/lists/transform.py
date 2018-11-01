# def transform(list1,list2,r1,r2):
#     """ Removes slice r1:r2 from list1 and append the slice to list2. """
#     sliced = list1[r1:r2]
#     sliced = sliced[::-1] # Reverse the slice
    
#     for i in range(r2-1,r1-1,-1):
#         list1.remove(list1[i])

#     list2.extend(sliced)

def transform(list1, list2, index1, index2):
    list1 = [list1.pop(index1) for element in range(index1, index2)]
    list1.reverse()
    list2 = [list2.append(element) for element in list1]
    return list2

def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

def get_integer(prompt):
    val = int(input(prompt))
    return val

# Main program starts here - DO NOT change it
list1 = get_list()
list2 = get_list()
index1 = get_integer("Enter from value: ")
index2 = get_integer("Enter to value: ")
transform(list1, list2, index1, index2)
print(list1)
print(list2)