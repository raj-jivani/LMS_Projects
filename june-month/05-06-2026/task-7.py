'''
write a python programme that reads a text file and counts the total number of words, characters, and lines in the file.
'''

file = open("notes.txt", "r")
content = file.read()

lines = content.splitlines()
total_lines = len(lines)

words = content.split()
total_words = len(words)

characters = len(content)

print("Total lines:", total_lines)
print("Total Words:", total_words)
print("Total character:", characters)

file.close()