'''
Check if a string starts with "Hello" and ends with "World".
- Remove all non-alphabatic characters from "Data123#Science!"
- Reverse the string "Python"
'''

sentence_1 = "Hello, Welcome to Python World"

print(sentence_1.startswith("Hello"))
print(sentence_1.endswith("World"))

sentence_2 = "Data123#Science!"
sentence_3 = ""

for i in sentence_2:
    if i.isalpha():
        sentence_3 += i

print(sentence_3)

word = "Python"
print(word[::-1])