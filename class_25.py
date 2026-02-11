# lambda function in python
# an annomous function used to define a function without any name in one line.
"""
Docstring for class_25
def double(x):
    return x * 2
double = lambda x : x * 2 
#  with two arguments 
def avg(x,y):
    return (x +y) / 2
double = lambda x,y : (x + y) / 2 

print(double(4,8)) 

# map function
# map function is used to apply a function on all elements of a list
l = [1,2,3,4,5,6]
def square(x):
    return x * x
# without map
emp_nl = []
for i in l:
    newl = i * i
    emp_nl.append(newl)
print(emp_nl) 

# with map function 

print(list(map(square, l))) # done with a single line of code

"""
# filter function
lst = [1,23,4,3,4,5,6,8]
def func_for_filter(x):
    return x > 3
# print(func_for_filter(3))

print(list(filter(func_for_filter , lst))) 

# reduce function
from functools import reduce

def func_for_reduce(x,y):
    return x + y
# reduce function interacts with whole list as a single item or object
print(reduce(func_for_reduce , lst)) 