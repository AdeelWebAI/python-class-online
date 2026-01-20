# raising custom errors in python 
# we can raise any custom error in python using raise keyword 
"""
Docstring for 19_class
cities = ["Queta","Lahore","Karachi","Peshawar","Islamabad",""]

a = input("Enter any capital from the cities in pakistan: ")
if a.capitalize() not in cities:
    raise ValueError("You not entered the city from capitals of pakistan")
print("Congratulatons ! , You understood raising error concept")

# lets do a quick quiz. 

# we have to write a python programe that if user input "pakistan" then python should not give any error.

"""
a = input("Enter string: ")

if a == "pakistan":
    pass 
if a != "pakistan":
    raise ValueError("You must enter the word pakistan to pass run this program smoethely") 
print("Congratulations ! You completed the quick quiz of class 19")

# also we can define an error by making a class of custome error

class error(Exception):
    pass 
    # we will come back here after reading classes in python..... 