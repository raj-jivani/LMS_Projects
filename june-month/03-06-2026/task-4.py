'''
Implement a class Account with private attribute balance.
- create methods to deposite nad withdraw money.
- add a method to display the balance
- ensure balance can not be accessed directly.
'''

class Account:
    def __init__(self):
        self.balance = 100000
    
    def deposite(self, amount):
        self.balance += amount
        
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def getBalance(self):
        return self.balance

a1 = Account()

a1.deposite(50000)
a1.withdraw(20000)
print(a1.getBalance())