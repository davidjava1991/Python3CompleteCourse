# Program to show named tuples with default values

from collections import namedtuple
Person = namedtuple("Person",
                    ["name","age","height"],
                    defaults=["David", 31, 180])
p1 = Person()
print("p1 = ", p1)
