'''
Implement a programme to create a function that returns a tuple containing the square and cube of given value
'''

def square_and_cube(num):
    square = num ** 2
    cube = num ** 3
    a = ()
    a += (square, )
    a += (cube, )
    return a

print(square_and_cube(3))
