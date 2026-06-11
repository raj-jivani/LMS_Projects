'''
write a python programme to open a text file read-write mode.
- read the existing content.
-append the line "This file was last modified by adding this sentence." to the file.
'''

file = open("demo.txt", "r+")
content = file.read()
print(content)

file.write("\n This file was last modified bu adding this line.")

file.close()