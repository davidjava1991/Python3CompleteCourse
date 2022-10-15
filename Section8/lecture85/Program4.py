# Program to show formatting of date time
from datetime import datetime

now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
str1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("str1:", str1)
str2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("str2:", str2)