# Constructors in python 

class Person:
    def __init__(self , n , o):
       self.name = n
       self.occ = o
    # name = "Adeel"
    # occ = "Developer"
    def info(self):
        print(f"Student's name is {self.name} and occupation is {self.occ}")


std1 = Person("python adeel","developer") 
std1.info()
std2 = Person("bahawal","ios developer") 
std2.info() 