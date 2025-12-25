# lists in python 
lst = [1,2,3,4,5,6,7,8,9]
"""
print(lst)
#we can store multiple data types in lists
lst2 = [1,2,3, "Adeel", True ]
#length of list 
print(len(lst)) 
# check the type of the list
print(type(lst))
#indexing and negative indexing in lists
print(lst[4]) 
print(lst[len(lst)-4])
determined_elements = []
for i in lst:
    if i < 7:
        determined_elements.append(i)
print(determined_elements)
# determine either a list have any specific element or not
if 2 in lst:
    print("Yes")
else:
    print("No") 
# list slicing (same as string slicing)
print(lst[1:5]) 
print(lst[1:4]) 
print(lst[3:]) 
print(lst[:5]) 
#slicing with jump index
print(lst[1:8:2]) 
#list comprehension 
comp_list = [i*i for i in lst]
print(comp_list) 
"""