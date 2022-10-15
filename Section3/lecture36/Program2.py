# Program to show methods of set

set1 = {1, 2, 3, 4}
set1.add(5)
print("after add = ", set1)
set2 = {6, 7, 8, 9}
print("union = ", set1.union(set2))
set3 = {4, 5, 6, 7}
print("intersection = ", set2.intersection(set3))
set1.discard(1)
print("after discard = ", set1)