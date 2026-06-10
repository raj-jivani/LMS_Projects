'''
write a programme to find the average of a 1D array without using any built in function.
'''

size = int(input("Enter size of array: "))

a = []

for i in range(size):
    value = int(input(f"a[{i}] = "))
    a.append(value)

count = 0
total_sum = 0

for i in a:
    count += 1
    total_sum += i

print(f"Average of 1D array: {total_sum / count}")
