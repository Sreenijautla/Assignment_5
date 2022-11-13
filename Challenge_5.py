# Challenge 5: Handling a Bank Account

import sys
class Account:
  def __init__(self, title=None, balance=0):
    self.title = title
    self.balance = balance
  def withdrawal(self, amount):
    if amount>self.balance:
      print("Insufficient balance, we cannot process your request")
      sys.exit()
    self.balance=self.balance-amount
    print("Balance amount after withdrawal is :", self.balance)
  def deposit(self, amount):
    self.balance=self.balance+amount
    print("Balance amount after deposit is :", self.balance)
  def getBalance(self):
    return self.balance
class SavingsAccount(Account):
  def __init__(self, title=None, balance=0, interestRate=0):
    super().__init__(title, balance)
    self.interestRate = interestRate
  def interestAmount(self):
    interest_amount=((self.interestRate)*self.balance)//100
    print("Interest amount is :", interest_amount)
#code to test - do not edit this
demo1 = SavingsAccount("Ashish", 2000, 5)
demo1.interestAmount()
print("Balance amount is :",demo1.getBalance())
demo1.deposit(500)
print("--------------------------------")
demo2 = SavingsAccount("Ashish", 2000, 5)
demo2.interestAmount()
print("Balance amount is :",demo2.getBalance())
demo2.withdrawal(500)