# Functions

# A set of code that is used to perform some task is called function
# there are two types of funtions in python first is built in functions and second is user defined functions


"""
# userdefined functions

a = 3
b = 4
def sum():
    print(a + b)
    if a > b:
        print("First number is greate")
    # else:
        print("Second number is greater")
sum()
# Funtions with arguments

def sumOfMarks(a,b,c):
    print(a + b + c)
    if a > b and a > c:
        print("First number is greater")
    elif b > a and b > c:
        print("Second number is greater")
    else:
        print("third number is greater")

sumOfMarks(1,4,3) 

def afterDefineFunction():
    pass
    
"""
# function to sum randon numbers

def sumRandomNumbers(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print(sum) 
    
sumRandomNumbers(3,4,5,56)


# built in funcitons

# built in functions are the functions that are built in functions in python you don't have to define their login for you code like range(), len() etc