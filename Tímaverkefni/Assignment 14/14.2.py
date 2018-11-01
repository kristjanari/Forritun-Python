import string
def get_word_list(file):
    a_string = file.read()
    for i in [",",".","?","!",":",";"]:
        a_string = a_string.replace(i,"")
    lower_string = a_string.lower()
    a_list = lower_string.strip("\n").split()
    return a_list

def word_list_to_counts(a_list):
    a_dict = {}
    for value in a_list:
        if value in a_dict:
            a_dict[value] += 1
        else:
            a_dict[value] = 1
    return a_dict

def dict_to_tuple(a_dict):
    a_list = []
    for key,value in a_dict.items():
        a_list.append((key,value))                
    return a_list

def main():
    filename = input("Name of file: ")
    # Get a file pointer
    fpointer = open(filename)
    # Get a list of words from the file
    word_list = get_word_list(fpointer) 
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list)
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuple(word_count_dict)
    #print(sorted(word_count_tuples))
    print(sorted(word_count_tuples))
    
main()