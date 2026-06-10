'''
develop a programme to demonstrate the difference between local and global variables with the same name.
'''

a = 10

def increase():
    global a
    a += 10
    return a

print(a)

print(increase())
