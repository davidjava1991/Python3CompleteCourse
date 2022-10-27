12# Program to show use of try except  block

try:
    n = int(input("Enter a number \n"))
    print(" You entered ", n)
except ValueError:
    print("That was not an int")


