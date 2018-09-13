# palindrome function definition goes here
def palindrome(setning):
    strengur = ""
    for stafur in setning:
        if stafur.isalpha():
            strengur += stafur
    strengur = strengur.lower()
    if strengur == strengur[::-1]:
        return True
    return False  

in_str = input("Enter a string: ")

# call the function and print out the appropriate message
if palindrome(in_str):
    print('"' + in_str + '"', "is a palindrome.")
else:
    print('"' + in_str + '"', "is not a palindrome.")
    