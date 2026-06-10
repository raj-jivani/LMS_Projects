'''
write a programme that opens a file, handles any exception if the file doesn't exist, and ensures the file is closed using the finally block
'''
try:
    filename = input("Enter file name: ")
    
    file = open(filename, "r")
    content = file.read()
    file.close()
except FileNotFoundError:
    print("File does not exist.")
else:
    print(content)
finally:
    print("file closed")