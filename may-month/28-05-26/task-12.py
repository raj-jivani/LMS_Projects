'''
create a function that calculate the area of rectangle
- add a __doc__ string to describe the function's purpose, parameters and return type
- write code to print the __doc__ string
'''

def area_of_rectangle(length, width):
    """this function calculate area of rectangle. In parameter we take lenght and width of rectangle and in return you get area in digits"""
    area = length * width
    return area

a = area_of_rectangle(10,20)

print(a)
print(area_of_rectangle.__doc__)