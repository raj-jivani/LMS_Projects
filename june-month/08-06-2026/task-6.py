'''
Create a programme that:
- Handle exception for invalid inputs and ensure a final message is displayed using the finally block, regardless of the outcome
'''
try:
    num1 = int(input("Enter number 1:"))
    num2 = int(input("Enter number 2: "))
    
    num3 = num1 / num2
except ZeroDivisionError:
    print("Can not divide by Zero")
except ValueError:
    print("Invalid Input")
except TypeError:
    print("Invalid Type")
else:
    print(num3)
finally:
    print("Programme Finished")