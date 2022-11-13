# Challenge 1: Square Numbers and Return Their Sum

class Point:
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
  def sqSum(self):
    x=self.x*self.x
    y=self.y*self.y
    z=self.z*self.z
    sum=x+y+z
    return sum
a=Point(1,3,5)
print("The total sum is :",a.sqSum())

# 2nd approach

class Point:
  x=1
  y=3
  z=5
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
  def sqSum(self):
    x=Point.x*Point.x
    y=Point.y*Point.y
    z=Point.z*Point.z
    sum=x+y+z
    return sum
a=Point(1,3,5)
print("The total sum is :",a.sqSum())