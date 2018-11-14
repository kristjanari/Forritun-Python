def get_number_of_shares():
    while True:
        try:
            return int(input("Enter number of shares: "))
        except:
            print("Invalid number")

def get_price():
    while True:
        try:
            price_string = input("Enter price (dollars, numerator, denominator) : ")
            price_list = price_string.split()
            return [int(i) for i in price_list]
        except:
            print("Invalid price!")

def print_info(num_of_shares, dollars, numerator, denominator):
    price = dollars + numerator/denominator
    value = num_of_shares*price
    print("{} shares with market price {} {}/{} have value ${:.2f}".format(num_of_shares, dollars, numerator, denominator, value))

def get_choice():
    return input("Continue: ")

def main():
    choice = "y"
    while choice.lower() == "y":
        num_of_shares = get_number_of_shares()
        dollars, numerator, denominator = get_price()
        print_info(num_of_shares, dollars, numerator, denominator)

main()