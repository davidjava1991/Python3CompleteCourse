# Program to show email validation  in Python

import re
str = "test@test.com"
pattern = r"[\w\.-]+@[\w\.-]+"
match = re.search(pattern, str)
if match:
    print("Found")
else:
    print("Not Found")
