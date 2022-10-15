# Program to show regular expressions in Python

import re
str1 = "David"
pattern = r"[a-z]+"
match = re.search(pattern, str1)
if match:
    print("Found")
else:
    print("Not Found")
