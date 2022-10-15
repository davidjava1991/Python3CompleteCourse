# Program to find largest of two numbers using if block

var1 = int(input("Enter number 1 \n"))
var2 = int(input("Enter number 2 \n"))
if var1 > var2:
    print("{} is greater than {}".format(var1, var2))
if var2 > var1:
    print("{} is greater than {}".format(var2, var1))