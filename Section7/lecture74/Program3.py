# Program to show regular expressions in Python

import re
str1 = ":david:"
pattern = r":(\w+):+"
find = re.findall(pattern, str1)
if find:
    print("Found")
    print(find)
else:
    print("Not Found")
