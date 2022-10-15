# Program to filter a dictionary

user_dict = {"David": 32, "Adam": 34, "Sam": 46,
             "Paul": 34, "John": 36}
filtered_dict = {x: y for (x, y) in user_dict.items() if y > 35}
print("filtered_dict = ", filtered_dict)