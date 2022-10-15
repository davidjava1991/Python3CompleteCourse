# Program to show Assertions in python

def print_age(age):
    assert(age>0),"Age must be greater than zero"
    print("Age = ",age)


print_age(20)
print_age(-1)  # Throws Assertion error

