import math

class MyString:
    
    def __init__(self, string):
        self.string = string

    def __sub__(self, other):
        self_length = len(self.string)
        other_legnth = len(other.string)
        return abs(self_length - other_legnth)

    def __gt__(self, other):
        return len(self.string) > len(other.string)

obj1 = MyString('this is a string')
obj2 = MyString('this is another one')
print(obj1 > obj2)
print(obj1-obj2)