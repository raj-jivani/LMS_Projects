'''
Perform the following operations on the given two sets:
    - Union
    - Intersection
    - Difference

set_A = {1,2,3,4}
set_B = {3,4,5,6}
'''
set_A = {1,2,3,4}
set_B = {3,4,5,6}

set_C = set_A.union(set_B)  # Union method
print(set_C)

set_D = set_A.intersection(set_B)   # Intersection method
print(set_D)

set_E = set_A.difference(set_B)     # Difference method
print(set_E)