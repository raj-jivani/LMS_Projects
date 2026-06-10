'''
Write a Python Programme to open an existing file in read mode and display its content.
- Open the file in write mode, overwrite the content, and write a new sentence "Learning file handling in python is fun."
'''

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

file = open("sample.txt", "w")
file.write("Learning file handling in python is fun.")
file.close()