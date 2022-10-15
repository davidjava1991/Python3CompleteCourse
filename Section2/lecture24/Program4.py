# Program to show scopes of variable in Python
var1 = 10


def change_value():
    var1 = 20


change_value()
print("value of var1 after method call is ",var1)