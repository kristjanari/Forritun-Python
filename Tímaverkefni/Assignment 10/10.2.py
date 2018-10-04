def to_list(a_string):
    a_list = a_string.split(",")
    if len(a_list) == 1:
        b_list = a_string.split()
        return b_list
    return a_list


# The main program starts here - DO NOT change it
the_string = input("Enter the string: ")
the_list = to_list(the_string)
print(the_list)