# Program to show global keyword
var2 = 10


def func():
    var1 = 30
    print("local var1 = ", var1)

    global var2
    var2 = 20
    print("global var2 = ", var2)


func()


