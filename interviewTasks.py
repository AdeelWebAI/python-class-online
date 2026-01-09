# print 

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *


for i in range(1,5):
    for space in range(5-i):
        print(" ",end="")
    for star in range(2*i-1): 
        print("*",end="") 
    print()

for i in range(3,0,-1):
    for space in range(5 - i):
        print(" ", end="")
    for star in range(2*i + -1):
        print("*",end="")
    print()
    
    
# make a function that return 
# 3 => 5
# 5 => 3

#without using if switch terminator

def change(n):
    return 8 - n

u_input = int(input("Enter number: "))

result = change(u_input)
print(result) 

# logical question
# 100 km long train
# 100 km long bridge
# speed 100km/h
# ----> ======= ---->

# answer is 2 hours 