'''
take a user input for a number:
    - check if it exists in array.
    - print the index if found, lese print not found.
'''

a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

while True:
    number = int(input("Enter number: "))
    
    if number in a:
        at = a.index(number)
        print(f"{number} is fount at index {at}")
        break
    else:
        print(f"{number} not found")