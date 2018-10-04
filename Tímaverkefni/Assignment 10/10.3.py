# Your functions should appear here
def populate_list(the_list): 
    while True:
        inp = input("Enter value to be added to list: ")
        if inp.lower() == "exit":
            break
        the_list.append(inp)

def triple_list(a_list):
    return a_list*3
# Main program starts here - DO NOT change it.
initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)