# Program to show filter function

list1 = [21, 54, 62, 35, 67, 34, 55, 57, 35, 45]


def checker(n):
    if n >= 50:
        return True
    else:
        return False


list2 = list(filter(checker, list1))
print("list2 = ", list2)

