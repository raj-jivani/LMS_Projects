'''
write a programme where a function splits a given string into two parts: 
- one containing only vowels.
- second contains all other characters
'''
def split_string(string):
    vowels = []
    constants = []
    a = str(string)
    a.lower()
    for i in string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vowels.append(i)
        else:
            constants.append(i)
    
    print(vowels)
    print(constants)

split_string("Hello")