def main():

    v1 = Vehicle("AB 123", 2010)
    c1 = Car("SF 735", 2007, "Station")
    t1 = Truck("TU 765", 1994, 6)
    b1 = Motorbike("XY 666", 2005)

    c1.set_weight(3500)
    t1.set_weight(9000)
    b1.set_CC(250)
    
    # Print info
    print(v1)
    print(c1)
    print("The weight of the car is: {:.2f}".format(c1.get_weight()))
    print(t1)
    print("The fee for the truck is: {:.2f}".format(t1.get_fee() ))
    print(b1)
    print("The CC of the bike is: {:.2f}".format(b1.get_CC() ))
    print()
    #Put the four vehicles into a list.
    # Then loop through the list and call the print function for each of the
    # vehicles.
    # You have to implement this part of the main program!
    # YOUR CODE GOES HERE
    vehicle_list = [v1, c1, t1, b1]
    for vehicle in vehicle_list:
        print(vehicle)

    v1 = c1
    print(v1)
    print()

main()
