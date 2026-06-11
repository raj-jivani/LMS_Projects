'''
create a python programme to demonstrate all modes (r,w,a,r+,w+,a+).
For each mode:
    - open a file, write or read depending on the mode.
    - close the file properly
'''

file = open("demo.txt", "r")
content = file.read()
print(content)
file.close()

file = open("c.txt", "w")
file.write("Hello, Raj here\n I am learning file handleing.")
file.close()

file = open("c.txt", "a")
file.write("\n doing practice task of file handling")
file.close()

file = open("demo.txt", "r+")
content = file.read()
print(content)

file.write("\n Good morning")
file.close()

file = open("demo.txt", "a+")
file.write("\n i used a+ mode in this file.")

content = file.read()
print(content)

file.close()
