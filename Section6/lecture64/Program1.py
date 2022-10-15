# Program to show single inherittance

class Vehicle:

    def __init__(self, number, colour):
        self.number = number
        self.colour = colour


class Car(Vehicle):
    pass


obj1 = Car(12332, "Red")
print("car details")
print(obj1.number)
print(obj1.colour)






