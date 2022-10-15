# Program to reverse a number

num = int(input("|Enter number \n"))
print("number = ", num)
rev = 0
while num != 0:
    rev = rev*10 + num%10
    num = num//10
print("reverse = ", rev)