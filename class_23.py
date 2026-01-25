# local and global Variables in python
"""
Docstring for class_23
x = 5 # x is a global variable
print(x) 
def hello():
    x = 10 # local variable 
    y = 3 # another local variable
    print(x) 
# we can access a global variable in a function but we can't access the local variable outside the functions 
    
hello()

# print(y) # it will return an error because y is a local variable 

        # global keyword
# if we want to change the value of global variable in a function , we use global keyword

"""
x = 10

def world():
    global x # uses the global variable to change
    x = 5 
    print(x) 
world() # output 5
print(x) # output 5 