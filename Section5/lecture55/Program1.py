
# Program to show map() function
list1 = [1, 2, 3, 4, 5]


def cube(n):
    return n**3


list2 = list(map(cube, list1))
print("list2 =", list2)