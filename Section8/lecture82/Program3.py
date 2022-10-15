# Program to show conversion of list and dict to a named tuple
list1 = [10, "David", 31]
from collections import namedtuple
Student = namedtuple("Student", ["id", "name", "age"])
stud1 = Student._make(list1)
print("stud1 : ", stud1)
dict1 = {"id": 43, "name": "Paul", "age": 43}
stud2 = Student(**dict1)
print("stud2 : ", stud2)

