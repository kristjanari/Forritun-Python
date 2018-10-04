def enter_number():
    while True:
        shares = input("Enter number of shares: ")
        try:
            shares_int = int(shares)
            return shares_int
        except ValueError:
            print("Invalid number!")

def enter_price():
    while True:
        price = input("Enter price (dollars, numerator, denominator): ")
        dollars, numerator, denominator =  price.split()
        try:
            dollars_int = int(dollars)
            numerator_int = int(numerator)
            denominator_int = int(denominator)
            numerator_int/denominator_int
            return dollars_int, numerator_int, denominator_int
        except ValueError:
            print("Invalid price!")
        except ZeroDivisionError:
            print("Invalid price, division by zero!")
        
        
def calculate_price(doll, nume, deno):
    price = doll + nume/deno
    return price

keep_going = "y"
while keep_going == "y":
    number_of_shares = enter_number()
    dollars, numerator, denominator = enter_price()
    price = calculate_price(dollars, numerator, denominator)
    value = number_of_shares*price
    print("{} shares with market price {} {}/{} have value ${:.2f}".format(number_of_shares, dollars, numerator, denominator, value))
    keep_going = input("Continue: ")
    
