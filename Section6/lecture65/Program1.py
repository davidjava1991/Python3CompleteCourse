# Program to show __str__ and __len__ Dunder methods

class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return "Student [id = {}, name = {}]".format(self.id,self.name)

    def __len__(self):
        return len(self.name)


obj1 = Student(1,"David")
print("str = ", obj1)
print("len = ", len(obj1))