# Program to find factorial of a number using while loop

n = num = int(input("Enter number \n"))
fact = num
while num > 1:
    fact *= num - 1
    num = num - 1
print("factorial of {} = {}".format(n, fact))