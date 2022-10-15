# Program to show multiple inheritance

class Father:

    def run(self):
        print("Father Running")


class Mother:

    def run(self):
        print("Mother running")


class Child1(Father,Mother):
    pass


class Child2(Mother,Father):
    pass


obj1 = Child1()
obj1.run()
obj2 = Child2()
obj2.run()
