# recursion in python
# recursion is the method in which we can call a function in the body of a function, here we are writing the table using recursion method
"""
def table(n, i=1):
    if i == 11:
        return 
    print(n, "X", i, "=", n * i) 
    table(n, i +1) 
    
table(2)
table(4)


# example of calculating factorial using recursion of function

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(6)) 

"""
# countdown example for practice 

def countdown(n):
    if n == 0:
        return 
    print(n)
    countdown(n-1) 
countdown(5)