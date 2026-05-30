'''
crete a list and tuple both containing the same 3 items
- Try changing the first item of each 
- Discuss the error (in case of tuple) and explain why it happens.
'''

li = [1,2,3,4,5]
tup = (1,2,3,4,5)

li[0] = 10
print(li)

tup[0] = 10
print(tup)  

# in tuple i am getting an error because tuple is immutable data type.