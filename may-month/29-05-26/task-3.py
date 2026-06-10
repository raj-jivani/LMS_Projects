'''
Develop a programme using recursion to reverse a string
'''

def reverse_string(string):
    if len(string) <= 1:
        return string
    
    return string[-1] + reverse_string(string[:-1])

text = input("Enter string: ")
print(f"Original string: {text}")
print(f"Reverse string: {reverse_string(text)}")
    