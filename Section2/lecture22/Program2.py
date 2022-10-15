# Program to find sum and average of n numbers
n = num = int(input("Enter the limit \n"))
total = 0
while n > 0:
    total = total + int(input("Enter number \n"))
    n = n - 1
print("Sum of Numbers : ", total)
print("Average of Numbers : ", total/num)



