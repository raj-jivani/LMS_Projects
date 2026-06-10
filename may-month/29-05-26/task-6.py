'''
create a lambda function to calculate the square of a number. 
- Use it inside a map() function to generate a list of squares from a given list of numbers.
'''

a = [2,4,6,8,10,12,14,16,18,20]

b = list(map(lambda x: x ** 2, a))

print(b)