class Rectangle:

    def __init__(self, length = 0, width = 0):
        if length >= 0:
            self.__length = length
        else:
            self.__length = 0
        if width >= 0:
            self.__width = width
        else:
            self.__width = 0
        

    def area(self):
        return (self.__length)*(self.__width)

    def perimeter(self):
        return 2*self.__length + 2*self.__width

    def __str__(self):
        return "Length: {}, Width: {}".format(self.__length, self.__width)

    def __eq__(self, other):
        return self.area() == other.area()

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__length, self.__width)

a = Rectangle(2,2)
b = Rectangle(2,3)
print(a)
print(a.area())
print(a.perimeter())
print(a.__repr__())
print(a == b)