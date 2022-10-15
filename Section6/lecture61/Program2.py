# Program to show classes and objects in Python

class Person:
    name = ""  # class attribute
    age = 0

    def run(self):
        print("Person running")

    def talk(self):
        print("Person talking")


person1 = Person()
person1.name = "David"
person1.age = 31
person1.run()
person1.talk()
print("-------------------------------")
person2 = Person()
person2.name = "Paul"
person2.age = 30
person2.run()
person2.talk()
