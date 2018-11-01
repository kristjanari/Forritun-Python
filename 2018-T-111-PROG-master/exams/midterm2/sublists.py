# A sublist is a list that makes up part of a larger list.
# The empty list, [], is a sublist of all lists.
#
# For example, the following are the sublists of the lists ['1','2','3']:
# [], ['1'], ['1', '2'], ['1', '2', '3'], ['2'], ['2', '3'], ['3']
#
# Write a program that displays the sublists of a given list.
# The program should contain at least one function, make_sublists(a_list), which
# returns a list of all the sublists of a_list
# Hint: List slicing is your friend!

def get_list():
    ''' Returns a list of strings input by a user. '''
    
    a_list = input('Enter a list separated with commas: ').split(',')
    return a_list

def make_sublists(a_list):
    ''' Returns a list of all the sublists of a_list '''
    length = len(a_list)
    sub_lists = [ [] ]
    for i in range(0, length):
        for j in range(i, length):
            a_slice = a_list[i:j+1]
            sub_lists.append(a_slice)
    return sub_lists

# Main program starts here
a_list = get_list()
sub_lists = make_sublists(a_list)
print(sorted(sub_lists))

