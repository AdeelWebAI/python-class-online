# --------  "Object Orientated Porgramming"   ----------
# concept of classes and objects and methods

"""
class Person:
    name = "Ali"
    age = 23
    height = 5.9
    print("Hi class")
    def info(self):
        print(self.name)
        print(self.age)
        print(self.height)
a = Person() 
print(a.info())
b = Person()
b.name = "Ahmad"
b.age = 33
b.height = 6.1
print(b.info())

# example 2 


class Car:
    def start(self):
        print("car has started !")
    def stop(self):
        print("car has stopped !")

a = Car() 

a.start()
a.stop() 
"""

# Example 3 

class Student:
    name = "Muneeb" 
    roll_no = 23
    marks = 98
    def info(self):
        self.name = "Rauf" # It will overwrite valuesss
        self.roll_no = 67
        self.marks = 70
        print(f"Student 1's name is {self.name}, Roll No is {self.roll_no} and Marks are {self.marks}")
        
std1 = Student() 
std1.info()
