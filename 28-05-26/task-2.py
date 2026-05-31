'''
Create a user-defined function(UDF) that calculates the factorial of a given number.
'''

result = 1

def factorial(n):
    if n == 0:
        return 0
    for i in range(1, n+1):
        global result
        result *= i
    return result

a = factorial(5)
print(a)