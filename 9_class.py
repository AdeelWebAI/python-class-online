"""
Function arguments and their uses
There are four types of functions arguments
1. required arguments
2. default arguments
3. keyword arguments
4. variable length arguments
"""

# required arguments
"""
def sum(a,b):
    print(a+b)
    
sum(3,4) 

#  default arguments 

def sum(a=3,b=4):
    print(a+b)
sum() 

# example in strings

def students(std1,std2="Hamza",std3="ali"):
    print("We have three students","1.",std1,"2.",std2,"3.",std3, "in our class")
students("Ahmad") 

# keyword arguments

def sum(a,b = 4, c = 5):
    print(a+b+c)
# sum(c=10, b= 22 ) 
sum(11,c=10, b= 22 ) 

# variable length arguments
#  in this method you can do operations with random numbers

def total(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The total of the given numbers are: \n",sum)
total(3,3,3,3,4,5,56,6) 
#  if we want to add dictionary as arguments

def students(**student):
    print("Hello", student["first"],student["second"],student["third"])
students(first="Ali",second = "Ahmad", third = "Adeel") 

# return statement

def sum(a,b):
    a+b
    return a+b

num = sum(2,3) 
print(num)

"""