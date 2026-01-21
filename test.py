def testFunction():
    print("Hi this is a test function to test import keyword")
    
def testForName():
    print("this is some text to understand __name__ in python")
if __name__ == "__main__":
    testFunction()
    testForName() 
print(__name__) 