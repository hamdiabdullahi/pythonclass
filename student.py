class Student:
     school = "AkiraChix"
     def __init__(self,name,age):
         self.name = name
         self.age = age
     def speak(self):
        return f"Hello class, my name is {self.name}"  
     def birthday(self):  
        return f"hello class,my name is {self.age}"  
    
        