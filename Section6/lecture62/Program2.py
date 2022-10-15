# Program to show constructors in python

class Employee:
    """ This is an employee class"""
    attr1 = "test" # class attribute

    def __init__(self, id, name, department):
        print("Constructor called")
        self.id = id # instance variables
        self.name = name
        self.department = department


obj1 = Employee(1, "David", "Accounting")
print("Employee details")
print(obj1.id)
print(obj1.name)
print(obj1.department)
print("accessing class attributes "+Employee.attr1)



