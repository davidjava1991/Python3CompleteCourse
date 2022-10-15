# Program to show advanced set methods

set1 = {1, 2, 3, 4, 5, 6}
set2 = { 4, 5, 6, 7, 8, 9}
print("difference() = ",set1.difference(set2))
print("symmetric_difference() = ",
      set1.symmetric_difference(set2))
print("isdisjoint", set1.isdisjoint({10, 11, 23}))