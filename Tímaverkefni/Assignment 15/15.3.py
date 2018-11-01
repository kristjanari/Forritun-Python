import string
import operator

def get_file_text_list():
    filename = input("Enter name of file: ")
    with open(filename) as f:
        a_string = f.read()
        a_string = a_string.strip("\n")
        for i in string.punctuation: #[",",".","?","!",":",";",'"']:
            a_string = a_string.replace(i,"")
    return a_string.split()

def make_key_tuples(a_list):
    key_tuple_list = []
    for index, value in enumerate(a_list):
        try:
            key_tuple_list.append((value,a_list[index+1]))
        except:
            None
    return key_tuple_list

def count_bigrams(a_tuple_list):
    count_dict = {}
    for a_tuple in a_tuple_list:
        if a_tuple in count_dict:
            count_dict[a_tuple] += 1
        else:
            count_dict[a_tuple] = 1
    return count_dict

def sorted_list(a_dict):
    sorted_list = sorted(a_dict.items(), key=operator.itemgetter(1))
    return sorted_list


word_list = get_file_text_list()
lower_word_list = [i.lower() for i in word_list]
key_list = make_key_tuples(lower_word_list)
the_dict = count_bigrams(key_list)
sorted_list = sorted_list(the_dict)
print(sorted_list[-10:][::-1])





