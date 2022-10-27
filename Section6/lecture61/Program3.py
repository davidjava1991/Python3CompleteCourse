# Program to show class object attributes


class Employee:
    company = "Udemy"  # Class attribute

    def __init__(self, name):
        self.name = name  # instance attribute


obj1 = Employee("David")
print(obj1.name)
print(obj1.company)
print(Employee.company)


