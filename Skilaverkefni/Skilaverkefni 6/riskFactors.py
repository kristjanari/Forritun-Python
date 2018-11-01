def header():
    print("{:33}{:33}{:21}".format("Indicator","Min","Max"))
    print("{:->87}".format(""))

def get_list(file):
    try:
        with open(file) as f:
            string = f.read()
            a_list = string.split("\n")
            data_list = []
            for line in a_list:
                data_list.append(line.split(","))
            data_list.pop()
            return data_list
    except:
        print("Cannot find file {}".format(file))

def clean_list(a_list):
    for item in a_list:
        for index, value in enumerate(item):
            item[index] = value.strip("%")
    return a_list

def disease_index(a_list):
    for index, value in enumerate(a_list[0]):
        if value == "Heart Disease Death Rate (2007)":
            heart_disease = index 
        elif value == "Motor Vehicle Death Rate (2009)":
            motor_vehicle = index    
        elif value == "Teen Birth Rate (2009)":
            teen_birth = index
        elif value == "Adult Smoking (2010)":
            adult_smoking = index
        elif value == "Adult Obesity (2010)":
            adult_obesity = index
    return heart_disease, motor_vehicle, teen_birth, adult_smoking, adult_obesity

def create_checklist(a_list,number):
    checklist = []
    for i in a_list[1:]:
        checklist.append(float(i[number]))
    return checklist

def create_statelist(a_list):
    statelist = []
    for i in a_list[1:]:
        statelist.append(i[0])
    return statelist

def maximum(a_list,number):
    checklist = create_checklist(a_list,number)
    the_max = max(checklist)
    for index,item in enumerate(checklist):
        if item == the_max:
            num = index
    statelist = create_statelist(a_list)
    return [statelist[num], the_max]
    
def minimum(a_list,number):
    checklist = create_checklist(a_list,number)
    the_min = min(checklist)
    for index,item in enumerate(checklist):
        if item == the_min:
            num = index
    statelist = create_statelist(a_list)
    return [statelist[num], the_min]

def print_stats(a_list,string,num):
    min_state,min_num = minimum(a_list,num)
    max_state,max_num = maximum(a_list,num)
    print("{:33}{:21}{:>6.1f}{:6}{:15}{:>6.1f}".format(string,min_state,min_num,"",max_state,max_num))

def the_list(filename):
    a_list = get_list(filename)
    a_list = clean_list(a_list)
    return a_list

def main_function():
    try:
        information = the_list(filename)
        heart_disease, motor_vehicle, teen_birth, adult_smoking, adult_obesity = disease_index(information)
        diseases_list = [["Heart Disease Death Rate (2007):",heart_disease],["Motor Vehicle Death Rate (2009):",motor_vehicle],["Teen Birth Rate (2009):",teen_birth],["Adult Smoking (2010):",adult_smoking],["Adult Obesity (2010):",adult_obesity]]
        header()
        for item in diseases_list:
            print_stats(information,item[0],item[1])
    except:
        header()

filename = input("Enter filename containing csv data: ")
main_function()
