from math import pi

class Circle:

    def __init__(self, radius):
        self.__radius  = float(radius)

    def __str__(self):
        return "Area: {:.2f}\nPerimeter: {:.2f}".format(self.get_area(), self.get_perimeter())

    def set_radius(self, new_radius):
        if new_radius > 0:
            self.__radius = new_radius

    def get_radius(self):
        return self.__radius

    def get_area(self):
        return pi*self.__radius**2

    def get_perimeter(self):
        return 2*self.__radius*pi


def main():   
    radius = input("Radius of circle: ")        
    circle = Circle(radius)
    print(circle)
    circle.set_radius(circle.get_radius() + 1.0)   
    print(circle)

main()