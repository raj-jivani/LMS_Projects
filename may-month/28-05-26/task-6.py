'''
Write a pyhton function that accepts an arbitary numbers of integer arguments and return their sum and product
'''

def sum_and_product(*args):
    a = sum(args)
    b = 1
    for i in args:
        b *= i 
    return a, b

c, d = sum_and_product(2,5,7,55,78)
print(c)
print(d)