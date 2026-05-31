'''
Convert the following:
    - A string '123' to an integer
    - A list[1,2,3] to a tuple
    - A list of pairs[(1,'A'), (2, 'B')] to  DICTIONARY
'''
a = "123"
b = int(a)

print(b, type(b))

c = [1,2,3]
d = tuple(c)

print(d, type(d))

e = [(1,"A"), (2,"B")]
f = dict(e)
print(f)