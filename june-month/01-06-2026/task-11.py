'''
create an array of numbers from 1 to 10
- multiply each element by 2 and print the result.
'''

a = [1,2,3,4,5,6,7,8,9,10]

b = [i ** 2 for i in a]

print(b)