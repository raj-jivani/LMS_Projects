'''
Create a dictionary from two lists:
keys = ['id', 'name', 'email']
values = [101, 'Bob', 'bob@example.com']
'''

keys = ['id', 'name', 'email']
values = [101, 'Bob', 'bob@example.com']

dict = {}

for i in range(len(keys)):
    dict[keys[i]] = values[i]

print(dict)