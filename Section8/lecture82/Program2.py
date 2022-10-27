# Program to show indexing and getattr() method in Named tuple

from collections import namedtuple

Customer = namedtuple("Customer", ["id", "name", "location"])
cust1 = Customer(21, "David", "India")
print("cust1 name = ", cust1[1])
print("cust1 location = ", getattr(cust1, "location"))