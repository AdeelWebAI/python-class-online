# Tuple manipulation and methods

students = ("ali","ahmad","hamza")
# this is a tuple that is immutable(unchangable) directly, if we have to chnage this tuples we have to convert it to a list and after changing we can change it to a tuple
"""
temp_students = list(students)
print(type(temp_students))
temp_students.append("ibrahim") # add item
temp_students.append("ismael") # add item
temp_students.remove("ahmad")  # remove item
temp_students.pop(1) # also remove item but also return
print(temp_students) 

students = tuple(temp_students)
print(students)
print(type(students)) 
# However we can change concatinate the two tuples 
students2 = ("rafay", "hadi")
all_students = students + students2
print(all_students) 
# some methods of tuple same as lists

print(students.count("ahmad")) # count the occurance of the item
print(students.index("ahmad")) # gives the first occurance of the item in index but if not found it throw the error
""" 
print(len(students)) # gives the length of the tuple
# ans so on all other list methods you can try on tuple ............