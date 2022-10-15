# Program to read a file using Python

f = open("Hello.txt", mode="r", encoding='utf-8')
content = f.read()
print(content)
f.close()
