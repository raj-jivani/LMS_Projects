'''
write a Python programme using a switch-case equivalent to:
    - Take an operator(=, -, *, /) as inputs.
    - Perform thr corresponding operation on two numbers entered by the user.
'''


n1 = int(input("Entre number1: "))
n2 = int(input("Entre number2: "))
operator = input("Input Operator: ")

match operator:
    case "+":
        print(f"Addition is {n1 + n2}")
    case "-":
        print(f"Subtraction is {n1 -n2}")
    case "*":
        print(f"Multiplication is {n1 * n2}")
    case "/":
        print(f"Divison is {n1 / n2}")
    case _:
        print("Invalid operator")

print("Task End")