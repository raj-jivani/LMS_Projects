'''
Develop a class Counter with an attribute count intialize to zero.
- Create methods to increment the count and display the value using self.
'''

class Counter:
    def __init__(self, count=0):
        self.count = 0
    
    def increment(self, number):
        self.count += number
        return self.count

c = Counter()
print(c.increment(5))
print(c.increment(15))