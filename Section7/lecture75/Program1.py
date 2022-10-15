# Program to show usage of iterator

tup = ("David", "Adam", "Paul", "Sam")
itr =iter(tup)
while True:
    try:   
        print("item = ", next(itr))
    except StopIteration:
        break
