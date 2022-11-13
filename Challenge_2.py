# Challenge 2: Implement a Calculator Class

class Calculator:
  def __init__(self,num1,num2):
    self.num1=num1
    self.num2=num2
  def add(self):
    print("The addition of num1 & num2 is :", self.num1+self.num2)
  def subtract(self):
    if self.num1>self.num2:
      print("The subtraction of num1 & num2 is :", self.num1-self.num2)
    else:
      print("The subtraction of num1 & num2 is :", self.num2-self.num1)
  def multiply(self):
    print("The multiplication of num1 & num2 is :", self.num1*self.num2)
  def divide(self):
    if self.num1>self.num2:
      print("The division of num1 & num2 is :", self.num1/self.num2)
    else:
      print("The division of num1 & num2 is :", self.num2/self.num1)
obj=Calculator(10,94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()