'''
Implement a function that takes a list of student names using *args and prints each name name on a new line.
- Add functionality to check if the list is empty and display a suitable message.
'''

def print_name(*args):
    if len(args) == 0:
        print("List of names are required")
    for i in args:
        print(i)

print_name("Raj", "hiren", "vandan", "jigar")