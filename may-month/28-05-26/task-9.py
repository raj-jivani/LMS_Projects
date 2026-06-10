'''
Write a function that accepts **kwargs to print out a formatted description of a person(e.g. name, age, city)
'''

def personInfo(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)

personInfo(name="Raj", age=23, city="Surat")