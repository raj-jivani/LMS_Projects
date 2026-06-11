'''
create a python programme that takes a word as input and searches for it in text file. 
- if found, diplay the line numbers where the word appears.
'''
word = input("Enter word: ")

file = open("notes.txt", "r")
content = file.read()

all_lines = content.splitlines()

for i in range(len(all_lines)):
    if word in all_lines[i]:
        print(f"your word is in {i + 1} line.")


file.close()