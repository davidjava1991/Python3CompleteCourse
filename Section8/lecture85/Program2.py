# Program to create custom date object
from datetime import date
a = date(2022, 4, 13)
print(a)
# from time stamp
timestamp = date.fromtimestamp(1426944364)
print("fromtimestamp() = ", timestamp)
