# Program to show dictionary comprehension

keys = ["David", "Paul", "Jose", "Adam"]
values = [32, 31, 39, 35]
user_dict = {x:y for (x,y) in zip(keys, values)}
print("user_dict = ", user_dict)

