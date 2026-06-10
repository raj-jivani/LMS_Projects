'''
Write a programme to input a file name fro the user, read its content, and handle any file-related exception.
- Use the else block to print the file content if no exception occurs.
'''
try:
    filename = input("Enter file name: ")
    
    file = open(filename, "r")
    content = file.read()
    file.close()
except FileNotFoundError:
    print("File is not exist")
else:
    print(content)