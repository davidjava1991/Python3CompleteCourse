# Program to show advanced methods in Dictionaries

user_dict = {"name": "David", "age": 31}
user_dict.setdefault("id", 0)
print("after set default : ", user_dict)
print("copy : ",user_dict.copy())
print("from keys = ",user_dict.
      fromkeys([1, 2, 3, 4, 5],0))
