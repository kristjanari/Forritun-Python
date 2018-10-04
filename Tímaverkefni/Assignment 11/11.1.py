
def mutate_list(a_list, index_num, v):
    ''' Inserts v at index index_num in a_list'''
    a_list.insert(index_num, v)
    
def remove_ch(a_list, index_num):
    ''' Removes character at index_num from a_list'''
    a_list.pop(index_num)
    
def get_list():
    ''' Reads in values for a list and returns the list '''
    user_list = input()
    user_list = user_list.split(",")
    user_list = [int(i) for i in user_list]
    return user_list

# Main program starts here
my_list = get_list()
print(my_list)
choice = input("Enter choice (m,r): ")
if choice.lower() == "m":
    index_number = input("Enter where you want to add a number and which number: ")
    index, number = index_number.split(",")
    index_int = int(index)
    number_int = int(number)
    mutate_list(my_list, index_int, number_int)
elif choice.lower() == "r":
    placement = int(input())
    remove_ch(my_list, placement)
print(my_list)
