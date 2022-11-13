# Challenge 3: Implement the Complete Student Class


class Student:
  # __name="Sree"
  # __rollNumber=77
  def setName(self,x):
    print("Setter Method_Name is called")
    self.__name=x
  def getName(self):
    print("Getter Method_Name is called")
    return self.__name
  def setRollNumber(self,y):
    print("Setter Method_rollNumber is called")
    self.__rollNumber=y
  def getRollNumber(self):
    print("Getter Method_rollNumber is called")
    return self.__rollNumber
a=Student()
a.setName("Sree")
print(a.getName())
a.setRollNumber(77)
print(a.getRollNumber())