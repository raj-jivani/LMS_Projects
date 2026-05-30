'''
Implement a program to :
- Take a string as input
- Print the string as reversed, and also print whther it is a aplindrome
'''

text = input("Entre a string: ")
reverse_text = text[::-1]

print(reverse_text)

if reverse_text.lower() == text.lower():
    print(f"{text} is palindrome")
else:
    print(f"{text} is not palindrome")