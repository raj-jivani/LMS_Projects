'''
Write a UDF that takes a string as input and returns the frequency of each character in the string
as a dictionary.
'''

def count_characters(string):
    cha_dict = {}
    for i in string:
        cha_dict[i] = string.count(i)
    return cha_dict

a = "Hello Raj, Welocme!"

b = count_characters(a)
print(b)