'''
write a lambda function that accepts three numbers and return the largest one.
'''

largest = lambda a, b, c: a if a >= b and a >= c else b if b >= c else c

print(largest(10,55,45))