'''
Create a list of squares of numbers from 1 to 10 using list comprehension.
- Create a new list that only contains even numbers from a given list [1,2,...,20]
- Convert all strings in a list ["hello", "WORLD", "pYtHOn"] to lowercase using list comprehension.
'''

square_list = []

for i in range(1,11):
    a = i ** 2
    square_list.append(a)

print(square_list)

even_numbers = []

for i in range(1,21):
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)

li = ["Hello", "WORLD", "pYtHOn" ]

new_li = [i.lower() for i in li]
print(new_li)