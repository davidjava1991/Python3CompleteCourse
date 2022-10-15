# Program to show use of self parameter

class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name


obj1 = Student(1, "David")
print("Student details")
print(obj1.id)
print(obj1.name)

