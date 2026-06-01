# Write a Programme in Pyhton to find the minimum number from the given three numbers using a nested if statement.

n1 = int(input("Entre number1: "))
n2 = int(input("Entre number2: "))
n3 = int(input("Entre number3: "))

if n1 < n2 and n1 < n3:
    print(f"Minimum number is {n1}")
elif n2 < n1 and n2 < n3:
    print(f"Minimum number is {n2}")
else:
    print(f"Minimum number is {n3}")