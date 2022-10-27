# Program to show use of self parameter in methods

class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getid(self):
        return self.id

    def setid(self, id):
        self.id = id


obj1 = Student(1, "David")
print("Student details")
print(obj1.id)
print(obj1.name)
print("using set and get methods")
obj1.setid(12)
print("id = ", obj1.getid())


