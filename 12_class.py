# tuples in python 
# most inportant is that tuples are not changeable
# tpl = (2,)
tpl = (1,2,3,4,5,6)
"""
print(type(tpl))
# we can print specific element in tuple using index same as list 
print(tpl[2]) 
print(tpl[4]) 
print(tpl[2]) 
# same as negatve indexing
print(tpl[-2])

#same as to find any specific number in tuples you can 

if 5 in tpl:
    print("5 is existing in the Tuple")
else:
    print("5 is not existing in the tuple") 
"""
#tuple slicing
# <Keep in mind that tuples are immutable but you can make a new tuple after slicing in existing tuple

tpl2 = tpl[2:4]
print(tpl2)

