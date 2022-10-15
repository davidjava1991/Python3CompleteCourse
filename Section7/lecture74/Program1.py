# Program to show regular expressions in Python

import re
str = "David"
pattern = r".vid"
match = re.search(pattern, str)
if match:
    print("Found")
else:
    print("Not Found")
