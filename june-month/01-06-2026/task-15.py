'''
print the first, last and middle element in 1D array.
'''
a = [12, 34, 55, 65, 43, 78, 89, 90, 12, 25, 48]

middle_element = len(a) / 2

print(f"First element: {a[0]}")
print(f"Last element: {a[-1]}")
print(f"Middle element: {a[round(len(a) / 2)]}")
