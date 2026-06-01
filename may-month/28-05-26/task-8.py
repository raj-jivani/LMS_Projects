'''
Develop a prgram where a UDF accepts *args and filters out the string from the arguments.
- Return a tuple of filtered values(e.g. string in one tuple, numbers in another)
'''

def filtered_values(*args):
    a = ()
    b = ()
    for i in args:
        if type(i) == str:
            a += (i,)
        elif type(i) in (int, float):
            b += (i,)
    print(a)
    print(b)

filtered_values("Raj",23,"deny",1.12,33,"hello", "A", "d", "FF")