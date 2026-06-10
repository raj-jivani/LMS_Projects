'''
- Write a programme that prompts the user to enter a number and attempts to find its square root.
- USe try to handle invalid input (e.g. negative number), else to print the square root of input,
  and finally to display a message like "Excution complete"
'''
def square_root(num):
    if num < 0:
        raise ValueError("can not find square root of negative number")
    return num ** 0.5

try:
    number = int(input("Enter number: "))
    result = square_root(number)
except ValueError as e:
    print(e)
else:
    print(f"Square root of {number} is {result}")
finally:
    print("Programme finished")