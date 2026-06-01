'''
Create a tuple of 5 numbers
- Access the third item in the tuple.
- Try to change the second value and observe the result(Explain mutability)
'''

tup = (1,2,3,4,5)
print(tup)

print(tup[2])  # accessing 3rd element in tuple

tup[1] = 45
print(tup)  # here i get an error because tuple is immutable data type.