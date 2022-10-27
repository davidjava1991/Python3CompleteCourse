# Program to show classes and objects in Python

class Person:

    def __init__(self,name, age):
        self.name = name  # instance attribute
        self.age = age


person1 = Person("David", 31)
print("person 1 name = ", person1.name)
print("person 1 age = ", person1.age)
person2 = Person("Paul",32)
print("person 2 name = ", person2.name)
print("person 2 age = ", person2.age)
