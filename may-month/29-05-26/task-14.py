'''
Write a function that takes a list of integers and returns the sum, maximum, amd minimum value as saperate results.
'''

def list_results(list):
    total_sum = sum(list)
    maximum = max(list)
    minimum = min(list)
    return total_sum, maximum, minimum

a = [12,23,45,67,76,45,34]

b = list_results(a)

print(f"Sum: {b[0]}")
print(f"Max: {b[1]}")
print(f"Min: {b[2]}")

