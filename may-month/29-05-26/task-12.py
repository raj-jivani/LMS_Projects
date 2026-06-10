'''
write a programme with two functions: one to intialize a global variable and another to increment it by a user defined value
'''


def intialize():
    global count
    count = 0

def increment(v):
    global count
    count += v
    print(count)

intialize()
increment(10)
increment(10)