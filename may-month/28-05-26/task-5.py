'''
Create a programme that takes a user defined function as an argument to calculate the cube of a list of a number
'''

def cube_list(list):
    list_cube = [i ** 3 for i in list]
    return list_cube

a = [1,2,3,4,5,6,7,8,9]

b = cube_list(a)
print(b)