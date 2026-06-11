'''
Write a python programme to open a file in binary mode
- use rb mode to read the content of text file and display its content in binary format.
'''

file = open("notes.txt", "rb")
content = file.read()
print(content)
file.close()