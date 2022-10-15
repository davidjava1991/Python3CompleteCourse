# Program to print a triangle of stars

pyramid = ""
length = 12
a = length//2
b = a+1
for n in range(0,length//2):
    for m in range(0, length +1):
        if a <= m < b:
            pyramid += "*"
        else:
            pyramid += " "
    a = a - 1
    b = b + 1
    pyramid += "\n"
print(pyramid)