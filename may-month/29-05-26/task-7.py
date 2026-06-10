'''
write a programme to filter out odd numbers from a list using a lambda function and filter() method.
'''

a = [2,4,6,7,4,3,89,64,56,43,24,12,34,55,67,87,88,100]

b = list(filter(lambda x: x % 2 != 0, a))

print(b)