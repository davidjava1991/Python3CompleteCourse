# Program to show kwargs in Python

def printer(**kwargs):
    for (k,v) in kwargs.items():
        print("key = ",k,", value = ",v)


printer(david=32, Paul=21, Adam=43, Sam=31)
printer(david=31)