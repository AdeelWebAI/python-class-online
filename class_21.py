#what is:     __name__ == "__main__"

#  if we have some functions executed in the another file which we are importing, they will run automatically in our main file.
import test
test.testFunction()
test.testForName() 

# to avoid this unwanted code execution, we use this check in our imported file (test.py)
# if __name__ == "__main__":
    # functions call 
print(__name__) 