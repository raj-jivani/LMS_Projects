'''Write a Program in pyhton to find the maximum number from the given four numbers using a nested if statement'''

n1 = int(input("Entre number1: "))
n2 = int(input("Entre number2: "))
n3 = int(input("Entre number3: "))
n4 = int(input("Entre number4: "))

if n1 > n2 and n1 > n3 and n1 > n4:
    print(f"Maximum number is {n1}")
elif n2 > n1 and n2 > n3 and n2 > n4:
    print(f"Maximum number is {n2}")
elif n3 > n1 and n3 > n2 and n3 > n4:
    print(f"Maximum number is {n3}")
else:
    print(f"Maximum number is {n4}")