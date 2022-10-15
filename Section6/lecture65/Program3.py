# Program to show __eq__ and __del__ dunder methods

class Person:

    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id

    def __del__(self):
        print("__del__() called")


obj1 = Person(12)
obj2 = Person(21)
obj3 = Person(21)

print(" comparing objects 1 and 2 - ", (obj1 == obj2))
print(" comparing objects 2 and 3 - ", (obj2 == obj3))





