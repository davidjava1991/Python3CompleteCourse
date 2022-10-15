# Program showing usage of super keyword

class Bird:

    def fly(self):
        print(" Bird fly()")


class Eagle(Bird):

    def fly(self):
        super(Eagle, self).fly()
        print("Eagle fly()")


obj1 = Eagle()
obj1.fly()
