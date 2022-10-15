# Program to show raising an exception

n = int(input("Enter numerator \n"))
d = int(input("Enter denominator \n"))
if d == 0:
    raise Exception("Denominator is zero")
else:
    print("division = ",(n/d))

