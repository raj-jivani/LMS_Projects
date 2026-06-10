'''
write a programme that tries to access an element in a list at non-existent index.
- Handle the exception using try.....except
'''

try:
    a = [12, 34, 55, 65, 43, 78, 89, 90, 12, 25, 48]
    
    ind = int(input("Enter index number: "))
    
    print(f"{a[ind]}")
except IndexError:
    print("Enter index is not available")
except ValueError:
    print("Invalid Input")