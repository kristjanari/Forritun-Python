class Vehicle:

    def __init__(self, the_license =  "", the_year = 0):
        self.license = the_license
        self.year = the_year
        self.weight = 0.0
        self.fee = 0.0

    def get_license(self):
        return self.license
    
    def get_year(self):
        return self.year
    
    def get_weight(self):
        return self.weight
    
    def get_fee(self):
        return self.fee
    
    def set_weight(self, new_weight):
        self.weight = new_weight

    def set_fee(self, new_fee):
        self.fee = new_fee

    def __str__(self):
        return "Vehicle: {} {} Weight={:.2f} Fee=${:.2f}".format(self.license, self.year, self.weight, self.fee)

class Car(Vehicle):

    def __init__(self, the_license = "", the_year = 0, the_style = ""):
        Vehicle.__init__(self, the_license, the_year)
        self.style = the_style

    def __str__(self):
        return "Car: {} {} {} Weight={:.2f} Fee=${:.2f}".format(self.license, self.year, self.style, self.weight, self.fee)

    def set_weight(self, new_weight):
        self.weight = new_weight
        self.fee = self.calculate_fee(self.weight)

    def calculate_fee(self, weight):
        if weight < 3000:
            return 30.0
        elif 3000 <= weight <= 5000:
            return 40.0
        else:
            return 50.0

class Truck(Vehicle):

    def __init__(self, the_license =  "", the_year = 0, wheels = 0):
        Vehicle.__init__(self, the_license, the_year)
        self.wheels = wheels

    def set_weight(self, new_weight):
        self.weight = new_weight
        self.fee = self.calculate_fee(self.weight)

    def __str__(self):
        return "Truck: {} {} {} wheels Weight={:.2f} Fee=${:.2f}".format(self.license, self.year, self.wheels, self.weight, self.fee)

    def calculate_fee(self, weight):
        if weight < 3000:
            return 40.0
        elif 3000 <= weight < 5000:
            return 50.0
        elif 5000 <= weight < 10000:
            return 60.0
        else:
            return 70.0

class Motorbike(Vehicle):
    
    def __init__(self, the_license =  "", the_year = 0):
        Vehicle.__init__(self, the_license, the_year)
        self.cc = 0

    def set_CC(self, cc):
        self.cc = cc
        self.fee = self.calculate_fee(cc)

    def get_CC(self):
        return self.cc

    def __str__(self):
        return "Motorbike: {} {} {} cc Fee=${:.2f}".format(self.license, self.year, self.cc, self.fee)

    def calculate_fee(self, cc):
        if cc < 50:
            return 10.0
        elif 50 <= cc < 200:
            return 20.0
        else:
            return 35.0


def main():

    v1 = Vehicle("AB 123", 2010)
    c1 = Car("SF 735", 2007, "Station")
    t1 = Truck("TU 765", 1994, 6)
    b1 = Motorbike("XY 666", 2005)

    c1.set_weight(3500)
    t1.set_weight(9000)
    b1.set_CC(250)
    
    #Print info
    print(v1)
    print(c1)
    print("The weight of the car is: {:.2f}".format(c1.get_weight()))
    print(t1)
    print("The fee for the truck is: {:.2f}".format(t1.get_fee()))
    print(b1)
    print("The CC of the bike is: {:.2f}".format(b1.get_CC()))
    print()
    
    vehicle_list = [v1, c1, t1, b1]
    for vehicle in vehicle_list:
        print(vehicle)

    v1 = c1
    print(v1)
    print()


main()

