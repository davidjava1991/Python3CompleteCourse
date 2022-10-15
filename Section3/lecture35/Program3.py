# Program to show tuple unpacking in Python

items = ("pen", "box", "ball", "paper")
(red, green, yellow, blue) = items
print("red = ",red)

list1 = [(1, 2), (3, 4), (5, 6)]  # llist of tuples
for (a, b) in list1:
    print("(",a,",", b, ")")