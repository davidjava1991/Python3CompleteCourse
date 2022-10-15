# Program to show both args and kwargs in same function

def print_function(*args, **kwargs):
    print("===== args =====")
    for a in args:
        print(a)
    print("========")
    print("=====kwargs=====")
    for (k,v) in kwargs.items():
        print("key = ", k,", value = ", v)


print_function(1, 2, 3, name="david", age=32, salary=300)


