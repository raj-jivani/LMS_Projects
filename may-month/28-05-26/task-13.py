'''
Develop a programme that uses a UDF to return the Fibonacci sequence up to a given number.
- include a detail __doc__ string explaining the function's working, input, and output
'''

def fibonacci(n):
    sequence = []
    a = 0
    b = 1
    
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

a = fibonacci(10)
print(a)