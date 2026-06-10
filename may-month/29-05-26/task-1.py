'''
Write a recursive function to calculate the factorial of a given number .
- Ensure the program handles edge cases
'''

def factorial(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(1)
print(result)