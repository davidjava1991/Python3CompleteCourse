# Program to find sum and average of n numbers
n = total = int(input("Enter the limit \n"))
sum = 0
while n>0:
    sum = sum + int(input("Enter number \n"))
    n = n - 1
print("Sum of Numbers : ", sum)
print("Average of Numbers : ", sum/total)



