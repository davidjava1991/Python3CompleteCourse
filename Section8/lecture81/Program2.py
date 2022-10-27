# Program to show operations on Counter

from collections import Counter

c1 = Counter({"a": 2, "b": 3, "c": 5})
c2 = Counter({"a": 4,  "b": 3, "c": 1})
print("c1 + c2 = ", (c1 + c2))
print("c2 - c1 = ", (c2 - c1))
print("c2 and c1 = ", c1 and c2)
print("c2 or c1 = ", c1 or c2)




