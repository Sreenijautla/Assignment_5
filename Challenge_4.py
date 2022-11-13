# Challenge 4: Implement a Banking Account

class Account:
  def __init__(self,title=0,Balance=0):
    self.title=title
    self.Balance=Balance
    print("Title is",self.title)
    print("Balance amount is",self.Balance)
class SavingsAccount(Account):
  def __init__(self,title=None,balance=0,interestRate=0):
    super().__init__(title, balance)
    self.interestRate=interestRate
    print("Interest Rate is",self.interestRate)
a=Account("Ashish",5000)
print("----------------------")
b=SavingsAccount("Ashish", 5000, 5)