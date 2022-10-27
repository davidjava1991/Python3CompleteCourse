# Program to show declaration and usage of Named tuple

from collections import namedtuple

Employee = namedtuple("Employee", ["id", "name", "department"])
emp1 = Employee(12, "David", "Management")
print("Employee Details")
print(emp1.id)
print(emp1.name)
print(emp1.department)
















3