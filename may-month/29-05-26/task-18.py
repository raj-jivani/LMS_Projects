'''
Create a function that takes a list of words and returns two lists: 
one with words start with vowels and the other with words starting with constants
'''

def split_list(li):
    vowels = []
    constants = []
    for i in li:
        i = str(i)
        j = i.lower()
        if j[0] == "a" or j[0] == "e" or j[0] == "i" or j[0] == "o" or j[0] == "u":
            vowels.append(i)
        else:
            constants.append(i) 
    
    print(vowels)
    print(constants)

a = ["Apple", "Raj", "Orange", "Dog", "umbrella", "123"]

split_list(a)
