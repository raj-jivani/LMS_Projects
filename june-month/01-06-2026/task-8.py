'''
write a programme to find the length of 1D array without using any built-in function
'''

size = int(input("Enter size of array: "))

a = []

for i in range(size):
    value = int(input(f"a[{i}] = "))
    a.append(value)

count = 0

for i in a:
    count += 1
    
print(f"lenght of array: {count}")
