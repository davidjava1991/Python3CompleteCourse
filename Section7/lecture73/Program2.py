# Program to show use of finally block
try:
    fop = open("Test.txt", mode="r", encoding="utf-8")
    print(fop.read())
except FileNotFoundError:
    print("File was not found")
finally:
    print("finally executed")