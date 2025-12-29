# f-strings in python 
# f strings are used to to formate strings in python and it is added after the python version 3.6 onward
# first we were formating strings like this method
"""
intro = "My name is {1} and I am from {0}"
name = "Adeel"
country = "Pakistan"

print(intro.format(country, name))

name = "Adeel"
country = "Pakistan"
income = 666.123445678
print(f"My name is {name} and I am from {country} and my income is {income:.6f} dollars per year") # :.2f means after point only 2 digits will print 

# if you want to print the {name} and {country} as it is in the string, you should use this method

print(f"My name is {{name}} and I am from {{country}}") 

calculation = f"{2*4}" # also we can perform calculations in f-string 
print(type(calculation)) 

"""
# doc string in python
# doc strings are not comments, these are strings that comes right after the definition of a function, method, class, or module

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5) 

print(square.__doc__)  