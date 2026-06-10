'''
Implement a recursive function to calculate the nth Fibonnaci number.
- Test the function with various inputs.
'''

def fibonnaci_sequence(num):
    if num <= 0:
        return 0 
    elif num == 1:
        return 1
    else:
        return (fibonnaci_sequence(num-1)) + (fibonnaci_sequence(num-2))

n = int(input("Enter value of n: "))

for i in range(n):
    print(fibonnaci_sequence(i), end=" ")
    