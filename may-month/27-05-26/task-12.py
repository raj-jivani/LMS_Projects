'''
create a set of integer: {1,2,3,4,5}.
Add 6, remove 3, and check if 2 is in the set.
'''

a = {1,2,3,4,5,6}

a.add(6) # adding element '6'
print(a)

a.remove(3) # removing elemet '3'
print(a)

print(2 in a)