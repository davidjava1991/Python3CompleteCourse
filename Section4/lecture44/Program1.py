# Program to print multiplication table using for in loop

for n in range(1, 10):
    print("Table of {}".format(n))
    for m in range(1, 10):
        print("{} x {} = {}".format(n, m, (n*m)))
    print("--------------------")
