'''
Implement a programme where a UDF accepts a list of integers and returns the square of each 
integer in a new list using list comprehension.
'''

def new_square_list(list):
    new_list = [i ** 2 for i in list]
    return new_list

a = [2,4,6,8,10]

b = new_square_list(a)
print(b)