# Main program starts here
def make_sublist(a_list):
    new_list = []
    new_list.append([])
    for i in range(1,len(a_list)+1):
        for k in range(0,i):
            new_list.append(a_list[k:i])
    return new_list

def get_list():
    command = input("Enter a list separated with commas: ")
    inp_list = command.split(",")
    return inp_list

input_list = get_list()
sub_lists = make_sublist(input_list)
# This should be the last statement in your main program/function 
print(sorted(sub_lists))

