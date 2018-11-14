def get_sum():
    a_sum = int(input("Input the cost of the item in $: "))
    return a_sum

def calculate_interest(the_sum):
    if the_sum <= 1000:
        return 0.015
    else:
        return 0.02

def the_payment(a_sum, interest_rate):
    interest_to_pay = a_sum*interest_rate
    a_sum += interest_to_pay
    if a_sum > 5000.0:
        payment = 5000.0
    else:
        payment = a_sum
    return a_sum, payment, interest_to_pay


def main():
    payment = 0
    month = 0
    total_interest_paid = 0
    the_sum = get_sum()
    interest_rate = calculate_interest(the_sum)
    while the_sum > 0:
        the_sum, payment, interest_paid = the_payment(the_sum, interest_rate)
        total_interest_paid += interest_paid
        the_sum -= payment
        month += 1
        print("Month: {} Payment: {:.2f} Interest paid: {:.2f} Remaining debt: {:.2f}".format(month, payment, interest_paid, the_sum))
    
    print()
    print("Number of months: {}".format(month))
    print("Total interest pais: {:.2f}".format(total_interest_paid))

main()