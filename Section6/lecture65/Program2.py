# Program to show __add__ and __new__ Dunder methods

class Employee:

    def __init__(self, id, name):
        print("__init__() callled")
        self.id = id
        self.name = name

    def __new__(cls, *args, **kwargs):
        print("__new__() called")
        inst = object.__new__(cls)
        return inst

    def __add__(self, other):
        return self.id + other.id



obj1 = Employee(12,"David")
obj1 = Employee(12, "David")

obj2 = Employee(2, "Paul")
print("add = ",obj1 + obj2)

