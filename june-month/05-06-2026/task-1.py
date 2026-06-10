'''
Write a python programme to create a text file named sample.txt
- Write the sentence "Pyhton is a versatile programming language." into the file.
'''

file = open("sample.txt", "w")
file.write("Python is a versatile programming language.")
file.close()