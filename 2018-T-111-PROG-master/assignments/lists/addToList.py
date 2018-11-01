def triple_list(a_list):
    ''' Returns a new list with 3 copies of every value in the given list '''
    return a_list * 3

def read_string():
    ''' Prompts for an input string and returns a lower case version of it '''
    input_str = input('Enter value to be added to list: ')
    return input_str.lower()

def populate_list(a_list):
  a_string = read_string()
  while a_string != 'exit':
      a_list.append(a_string)
      a_string = read_string()

# Main program starts here - DO NOT change it.
initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)
