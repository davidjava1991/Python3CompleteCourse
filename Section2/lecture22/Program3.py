# Program to print factorial of a given number

def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)


num = int(input("Enter the Number \n"))
print("Factorial of ", num," is ", factorial(num))