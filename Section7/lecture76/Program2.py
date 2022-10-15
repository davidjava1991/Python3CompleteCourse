# Program to generate fibonacci series

def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


obj = fib(6)
print("series:")
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

