# If-Else Statements
# if, elif, else logic
"""
Docstring for 5_class
age = int(input("Enter your age: "))

if age > 0 and age < 13:
    print("you are a kid")
elif age > 13 and age < 20:
    print("you are a teenager")
elif age > 20 and age < 40:
    print("you are a senior citizen")
elif age > 40 and age < 100:
    print("you are a old man")
else:
    print("your input is wrong")



nested if else


a = 11

if a > 10:
    print("a is greater than 10")
    if a == 11:
        a += 1
        print(a)
elif a == 9:
    print("a is equal to 9")
else:
    print("a is smaller than 10")



# short hand if else statement
"""

a = 33
b = 33

# print("A") if a > b else print("=") if a == b else print("B") 

# a simple example 
print("A and B are equal ") if a == b else "" 


# Calculator using short hand if else statement

num1 = int(input("Enter first Number: "))
opr = str(input("Enter the operation: "))
num2 = int(input("Enter second Number: ")) 

print(num1 + num2) if opr == "+" else print(num1 - num2) if opr == "-" else print(num1 * num2) if opr == "*" else print(num1 / num2) if opr == "/" else print("Sorry! Please Enter a valid operator") 

print("Sorry! An error occured, Maybe you Entered invalid operator") 

# another simple example
# a = 3
# b = 5
# c = 3 if a >b else 0

# print(c) 


# enumerate function in python 

# enumerate function is used to print the index number with the loop 

marks = [12,23,43,54,65,76,34,65]

for index, mark in enumerate(marks, start=1):
    print(f"student number {index} has the marks:{ mark}")