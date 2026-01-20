# loops in python 

"""
# for loop at numbers

for i in range(5):  # it will print the numbers 0 to 4
    print(i)
    
for i in range(10,100,5): # it will print numbers 10 to 100 with step of 5
    print(i)
    
# for loop and nested for loop at list 
"""

'''
# for loop at strings

me = "Adeel Waraich"

for i in me:
    print(i)
    if (i == "e"):
        print("e is special character")

# for loops on lists

names = ["Adeel","Ahmad","Hamza","Abadullah"] 

for name in names:
    print(name)
    for n in name:
        print(n) 
'''

# while loops

# while loop at numbers
'''
i= 0

while i <= 5:
    print(i)
    i = i + 1 
while i >0:
    i = i-1
    print(i) 

# while loops at strings
word = "AI"  
i = 0

while i < len(word):
    print(word[i])
    i += 1

# else statement with while loop

i = 0 
while i <=5:
    print(i)
    i = i+1
else:
    print("we have reached at number", i-1) 
i = i -2
while i >= 0:
    print(i)
    i = i -1 
# while loop with complex conditions
#  thsi loop will continuesly taking input from the user until the number is greater than 30 or smaller than 10
i = int(input("Enter the Number: "))
while i <30 and i >10:
    i = int(input("Enter the Number: "))
    print(i)
# break and continue statements

for i in range(11):
    if i == 3:
        print("This iteration will skipped")
        continue # continue statement skipps the loop
    if i == 6:
        print("The loop is ended here")
        break # break statement breaks the loop
    print(i) 
'''