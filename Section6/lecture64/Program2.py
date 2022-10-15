# Program to show method overriding

class Bird:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print("Bird flying")


class Duck(Bird):

    def fly(self):
        print("Duck Cannot fly")


obj1 = Duck("Donald")
obj1.fly()


