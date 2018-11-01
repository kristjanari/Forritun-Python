def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True

def get_input_list():
    command = input("Enter integers separated with commas: ")
    input_list = command.split(",")
    try:
        int_list = [int(i) for i in input_list]
        return int_list
    except:
        print("Incorrect input!")

def sort_list(a_list):
    a_list.sort()
    return a_list

def get_prime_list(a_list):
    prime_list = []
    for value in a_list:
        if is_prime(value):
            prime_list.append(value)
    return prime_list
    
def get_unique_list(a_list):
    new_list = []
    for value in a_list:
        if value not in new_list:
            new_list.append(value)
    return new_list

def get_min(a_list):
    return min(a_list)

def get_max(a_list):
    return max(a_list)

def get_average(a_list):
    return sum(a_list)/len(a_list)

# The main program starts here
main_list = get_input_list()
if main_list:
    print("Input list:",main_list)
    print("Sorted list:",sort_list(main_list))
    print("Prime list:",sort_list(get_unique_list(get_prime_list(main_list))))
    print("Min: {}, Max: {}, Average: {:.2f}".format(get_min(main_list),get_max(main_list),get_average(main_list)))