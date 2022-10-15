# Program to show methods of orderedDict

from collections import OrderedDict
emp_dict = OrderedDict()
emp_dict["name"] = "David"
emp_dict["id"] = 12
emp_dict["department"] = "Accounting"
print("emp_dict details : ",emp_dict)
emp_dict.update({"location": "India"})
print("emp_dict details after update: ", emp_dict)
emp_dict.move_to_end("name", last=True)
print("emp_dict after move_to_end : ", emp_dict)

