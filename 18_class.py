# else condtion with loops 
"""
for i in range(5):
    print(i)
    if i == 4:
        break
    
else:
    print("You conting have been completed") # else condition will loop execute only when loop is executed completely otherwise its will not execute 
# exception handling in python

# we can handle errors and also make the beautify according to our situation in python
def table():    
    a = int(input("Enter a Number to see its Table: "))
    print(f"Multiplication table of {a}") 
    for i in range(1,11):
        print(a ,"X", i,"=", i *a) 
        
try:
    table()
except:
    print("Sorry you program could not be executed") 
    
#finally keyword in python

# finally keyword often use with the try except and it always executed
try:
    x = int(input("Enter a Integer: "))
    print(x)
except:
    print("Sorry! You have not entered Integer") 
    
finally:
    print("This code will always eecuted") 
    
# it often uses when we have to use this type of code inside a function and returning something
"""
def test():
    try:
        a = int(input("Enter an integer"))
        b = a/0
        return print(a) 
    except:
        return print("Sorry Your code could not be executed") # function ended from here !
    finally:
            print("close all the files")
    print("This code will always run")  # this code will not run ever, we write it in finally keyword to run it always
test()
