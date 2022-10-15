# Program to show decorators in Python

def dec_func(original_func):
    def wrap_func():
        print("before call");
        original_func();
        print("After call");
    return wrap_func;


@dec_func
def need_decoration():
    print("inside need decoration");


need_decoration();