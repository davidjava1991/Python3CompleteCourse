# Program to show features of python functions

def fun1():
    print("from fun1")


fun2 = fun1
fun2()


def fun3(fun):
    fun()

fun3(fun2)




