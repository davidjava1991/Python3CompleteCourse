# Program to create a custom exception

class ArithmeticException(Exception):
    pass


try:
    raise ArithmeticException("Number is Zero")
except ArithmeticException:
    print("Custom Exception Thrown")

