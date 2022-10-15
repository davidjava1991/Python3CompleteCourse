# Program to show generators in Python

def num_gen(limit):
    i = 0
    while i < limit:
        i = i + 1
        yield i


for n in num_gen(5):
    print(" n = ", n)
