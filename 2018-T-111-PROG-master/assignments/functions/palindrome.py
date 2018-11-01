def palindrome(s):
    '''Returns True if the given string is a palindrome and False otherwise.'''
    s1 = ''
    for ch in s:
        if ch.isalnum():
            s1 += ch.lower()
    return s1 == s1[::-1]

in_str = input("Enter a string: ")
print('"{:s}" is '.format(in_str),end='')
if not palindrome(in_str):
    print("not ", end = '')
print("a palindrome.")