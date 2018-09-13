# The function definition goes here
def er_a_bili(a):
    if 1 < a < 555:
        return True
    else:
        return False

num = int(input("Enter a number: "))
# You call the function here
if er_a_bili(num):
    print(num, "is in range.")
if er_a_bili(num) == False:
    print(num, "is outside the range!")