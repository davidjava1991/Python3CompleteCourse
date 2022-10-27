# Python program to check a number is even or odd


def checkEven(num):
    if num%2 == 0:
        return True
    else:
        return False


n = int(input("Enter Number \n"))
if checkEven(n):
    print(n, " is Even")
else:
    print(n, " is Odd")
