'''
create a class person with attributes such as name and age.
- write a method to diplay the detils.
- create multiple objects and call the method for each.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

p1 = Person("raj", 23)
p2 = Person("hiren", 24)
p3 = Person("vandan", 22)

p1.display()
p2.display()
p3.display()