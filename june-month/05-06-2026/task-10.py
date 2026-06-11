'''
write a python programme to read content from an existing file and copy it to another file.
'''

file = open("notes.txt", "r")
content = file.read()

lines = content.splitlines()

file.close()

file = open("b.txt", "w")
for i in lines:
    file.write(f"{i} \n")
file.close()