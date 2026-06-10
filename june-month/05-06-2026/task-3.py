'''
Write a python programme to read and print the contents of the file simple.txt line by line.
'''

file = open("sample.txt", "r")
content = file.readlines()
print(content)
file.close()