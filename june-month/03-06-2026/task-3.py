'''
Write a programme to create a class Book with private attributes title and author.
- Add public methods to set and get these attributes
'''

class Book:
    def __init__(self):
        pass
        
    def setinfo(self, title, author):
        self.title = title
        self.author = author
        
    def getinfo(self):
        return self.title, self.author

b1 = Book()

b1.setinfo("all the best", "rohit shetty")
print(b1.getinfo())