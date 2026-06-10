'''
Create a python programme that writes multiple lines of text to a file named notes.txt.
- The Content
Line 1: Python is easy to learn
Line 2: It has numerous libraries.
Line 3: File handling is one of its feature
'''
lines = [
    "Line 1: Python is easy to learn \n",
    "Line 2: It has numerous libraries \n",
    "Line 3: File handling is one of its feature \n"
]

file = open("notes.txt", "w")
file.writelines(lines)
file.close()