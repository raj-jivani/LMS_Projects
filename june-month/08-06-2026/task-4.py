'''
Write a programme that tries to access an element in a string at non-existent index. 
- Handle exception, and use the else block to print the result if no exception occurs
'''

try:
    a = "Hello Python"
    result = a[2]
except IndexError:
    print("Invalid Index")
else:
    print(result)