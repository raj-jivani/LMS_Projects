'''
create a programme that:
    - iterates over a string(e.g. "PYTHON").
    - uses a continue statement to skip vowels and print only constants
'''

word = "HELLO PYTHON"

for i in word:
    if(i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
        continue
    print(i)

print("Task END")