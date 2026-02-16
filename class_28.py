#  decorators in python
"""
Docstring for class_28
def greet():
    print("before hi")
    print("Hi! Python Class")
    print("after hi")
    
"""

def greet_decorator(function):
    def function_wrapper():
        print("before greeting code.....")
        function() 
        print("after greeting code.....")
    return function_wrapper
    
@greet_decorator
def greet():
    print("Hi decorated class") 
    
greet()