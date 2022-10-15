# Program to show args and normal arguments together

def add(types="int", *args):
    if types == "int":
        add = 0
        for n in args:
            add += n
        return add
    elif types =="float":
        add = 0.0
        for n in args:
            add += n
        return add
    else:
        return 0


print("float add = ",add("float", 1.22,
                         2.45, 3.34, 4.45, 5.34))
print("int add = ", add("int", 1, 2, 3, 4, 5))

