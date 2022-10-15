# Program to write a file

with open("MyFile.txt", mode="w",  encoding='utf-8') as f:
    f.write("This file is Generated Buy Python")
print("File Written")