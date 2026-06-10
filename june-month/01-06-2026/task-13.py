'''
In a user defined array:
    - print all even numbers
    - print all odd numbers
'''

size = int(input("Enter size of array: "))

a = []

for i in range(size):
    value = int(input(f"a[{i}] = "))
    a.append(value)

for i in a:
    if i % 2 == 0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")

