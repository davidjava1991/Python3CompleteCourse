# Program to show *args in Python

def add(*args):
    add = 0
    for n in args:
        add += n
    return add


print("add() = ", add())
print("add(12) = ", add(12))
print("add(10,20) = ", add(10, 20))
print("add(1,2,3,4) = ", add(1, 2, 3, 4))



