'''
Write a python programme to append "Line 4: Python supports multiple modes of file handling." to the file notes.txt
'''

file = open("notes.txt", "a")
file.write("Line 4: Python supports multiple modes of file handling. \n")
file.close()