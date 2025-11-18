# match case statements

# simple example
"""
fruite = input("enter any fruite name: ")

match fruite:
    case "apple":
        print("this is an apple")
    case "banana":
        print("this is a banana")
    case _:
        print("is any other fruite")  
    """

# little bit hard example
# multiple values in a case
'''
day = input("Enter a day of week (monday to friday): ")

match day:
    case "Monday" | "Tuesday" |"Wednesday"|"Thursday"|"Friday":
        print(f"{day} is a working day")
    case "Saturday" | "Sunday":
        print(f"{day} is a weekend")
        
        '''
        
"""
point = (10, 20)

match point:
    case (0, 0):
        print("Origin point")
    case (x, y):
        print(f"X = {x}, Y = {y}")
"""

# more cases of default case 

x = int(input("Enter the Value of x: "))

match x:
    case 10:
        print("The value of x is ", x)
    case 40:
        print("The value of x is ", x)
    case ـ if x > 10 and x < 20:
        print(x,"is between 10 and 20")
    case ـ if x > 20 and x < 30:
        print(x,"is between 20 and 30")
    case ـ if x > 30 and x < 40:
        print(x,"is between 30 and 40") 
    case _:
        print("Please enter the number in range of 0 to 40") 