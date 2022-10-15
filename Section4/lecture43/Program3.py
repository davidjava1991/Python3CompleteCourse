# Program to find largest of three numbers

var1 = int(input("Enter number 1: \n"))
var2 = int(input("Enter number 2: \n"))
var3 = int(input("Enter number 3: \n"))
if var2 > var1:
    largest = var2
elif var1 > var2:
    largest = var1
if var3 > largest:
    largest = var3
print("largest value among {},{} and {} is {}"
      .format(var1, var2, var3, largest))