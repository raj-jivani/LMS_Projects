'''
Split "apple,banana,grapes" into a list
- Join the list ["Python", "is", "awesome"] into a sentence using spaces.
- Split a multiline string into seprate lines and print them one by one.
'''

fruits = "apple,banana,grapes"

fruit_list = list(fruits.split(","))
print(fruit_list)

words = ["python", "is", "awesome"]

sentence = " ".join(words)
print(sentence)

long_Str = "Hello, I am Raj. I am learning Python"
seprate_Str = long_Str.split(". ")

for i in seprate_Str:
    print(i)
