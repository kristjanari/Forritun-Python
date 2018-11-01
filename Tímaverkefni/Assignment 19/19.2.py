def read_data_from_file(file):
    with open(file) as f:
        file_string = f.read()
    file_list = file_string.split("\n")
    file_list = [float(i) for i in file_list]
    return file_list

class Sales:

    def __init__(self, data):
        self.__data = data

    def get_average(self):
        return sum(self.__data)/len(self.__data)

    def add_sale(self, sale):
        self.__data.append(sale)



def main():
    data = read_data_from_file("sales.txt")
    sales = Sales(data)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))
    sales.add_sale(78.5)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))

main()