# Program to show custom iterators

class Student:

    def __init__(self, *args):
        self.limit = len(args)
        self.args = args

    def __iter__(self):
        self.pos = 0
        return self

    def __next__(self):
        pos = self.pos
        if pos >= self.limit:
            raise StopIteration
        else:
            self.pos = pos + 1
        return self.args[pos]


obj1 = Student("David", "Paul", "Adam")
itr = iter(obj1)
while True:
    try:
        print("item = ", next(itr))
    except StopIteration:
        break
