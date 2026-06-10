'''
In 1D array:
    - print the first five elements
    - print every alternate element of an array.
'''
a = [12, 34, 55, 65, 43, 78, 89, 90, 12, 25, 48]

print("First Five Elements:", a[:5])

for i in range(0, len(a), 2):
    print(f"{a[i]}")

