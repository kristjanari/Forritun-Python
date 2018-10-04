
def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

def get_integer(prompt):
    val = int(input(prompt))
    return val

def transform(listi1, listi2, r1, r2):
    slicing = listi1[r1:r2]
    slicing_reversed = slicing[::-1]
    listi2.extend(slicing_reversed)
    teljari = r1
    for i in range(r1,r2):
        listi1.pop(r1)
    
# Main program starts here - DO NOT change it
list1 = get_list()
list2 = get_list()
index1 = get_integer("Enter from value: ")
index2 = get_integer("Enter to value: ")
transform(list1, list2, index1, index2)
print(list1)
print(list2)