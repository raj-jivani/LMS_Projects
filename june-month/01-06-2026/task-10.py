'''
Write a programme to perform addition operation between two 1D array and store in another array. 
Keep in mind that both array size must be the same.
'''
size = int(input("Enter size of array: "))

a = []
b = []

for i in range(size):
    value = int(input(f"a[{i}] = "))
    a.append(value)

for i in range(size):
    value = int(input(f"b[{i}] = "))
    b.append(value)

c = []

for i in range(size):
    d = a[i] + b[i]
    c.append(d)

print(c)