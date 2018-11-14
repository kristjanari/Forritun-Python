def get_filename():
    return input("Enter filename containing csv data: ")

def get_data_from_file():
    while True:
        try:
            filename = get_filename()
            with open(filename) as f:
                data_string = f.read()
            return data_string
        except:
            print("Cannot find file {}".format(filename))

def clean_list(a_list):
    for index, value in enumerate(a_list):
            a_list[index] = value.strip("%")

def create_data_dict(data_string):
    data_list = data_string.split("\n")
    data_list.pop()
    data_dict = {}
    for item in data_list:
        item_list = item.split(",")
        clean_list(item_list)
        data_dict[item_list.pop(0)] = item_list
    return data_dict

def create_disease_dict(index, data_dict):
    disease_dict = {}
    for key in data_dict:
        try:
            disease_dict[key] = float(data_dict[key][index])
        except:
            pass
    return disease_dict
        
def find_maximum(disease_dict):
    the_max = 0
    for key, value in disease_dict.items():
        if value >= the_max:
            the_max = value
            max_state = key
    return (max_state, the_max)
    
def find_minimum(disease_dict):
    the_min = 10000 
    for key, value in disease_dict.items():
        if value <= the_min:
            the_min = value
            min_state = key
    return (min_state, the_min)

def create_max_min_dict(data_dict):
    max_min_dict = {}
    for index, a_disease in enumerate(data_dict["State"]):
        disease_dict = create_disease_dict(index, data_dict)
        max_info = find_maximum(disease_dict)
        min_info = find_minimum(disease_dict)
        max_min_dict[a_disease] = {"max": max_info, "min": min_info} 
    return max_min_dict

def print_header():
    print("{:<37}{:<33}{:<21}".format("Indicator", "Min", "Max"))
    print("_"*91)

def print_result(main_dict):
    print_header()
    for disease in main_dict:
        max_state = main_dict[disease]["max"][0]
        max_num = main_dict[disease]["max"][1]
        min_state = main_dict[disease]["min"][0]
        min_num = main_dict[disease]["min"][1]
        print("{:<37}{:<21}{:>6.1f}      {:<15}{:>6.1f}".format(disease, min_state, min_num, max_state, max_num))

def main():
    data = get_data_from_file()
    data_dict = create_data_dict(data)
    main_dict = create_max_min_dict(data_dict)
    print_result(main_dict)

main()