# Your function definition goes here
def count_case(strengur):
    storir = 0
    litlir = 0
    for stafur in strengur:
        if stafur.isupper():
            storir += 1
        elif stafur.islower():
            litlir += 1
    return storir, litlir

user_input = input("Enter a string: ")

# Call the function here
upper, lower = count_case(user_input)

print("Upper case count: ", upper)
print("Lower case count: ", lower)