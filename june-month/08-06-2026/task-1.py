'''
Develop a programme that divides two number provided by user.
- use try.....except to handle division by zero
'''

try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    num3 = num1 / num2
    print(num3)
except ZeroDivisionError:
    print("Can not divide by zero")
except ValueError:
    print("Invalid input")