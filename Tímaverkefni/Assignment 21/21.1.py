CANDY_PRICE = 1.5

def amount_of_money(choice):
    money_dict = {"n": 0.05, "d": 0.10, "q": 0.25, "D": 1.0}
    try:
        return money_dict[choice]
    except:
        print("'{}' is not a valid coin.".format(choice))
        return 0.0

def print_options():
    print("Please insert coins:")
    print("\tn - Nickel\n\td - Dime\n\tq - Quarter\n\tD - Dollar")

def get_choice():
    print_options()
    choice = input()
    return choice

def print_info(total_amount):
    print("A packet of candy costs $ {:.2f}. You have inserted $ {:.2f}.".format(CANDY_PRICE, total_amount))


def main():
    total_amount = 0.0
    while total_amount < 1.5:
        print_info(total_amount)
        choice = get_choice()
        total_amount += amount_of_money(choice)
    print("Enjoy your candies. Your change is $ {:.2f}. Please visit again.".format(total_amount-CANDY_PRICE))

main()