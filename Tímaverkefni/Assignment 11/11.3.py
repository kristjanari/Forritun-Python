
def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

def even_sum(listi):
    nýr_listi = [int(i) for i in listi if int(i)%2 == 0]
    return sum(nýr_listi)

# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))
