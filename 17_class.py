# dictionaries in python
# dictionaries are the data types in python which are used to store and manipulate data in key pair values.


dic = {"name":"Adeel", "Marks": 60 , "is_educated":True} 
"""
print(dic) # print dictionary
print(dic["is_educated"]) # print specific value of the key
print(dic.keys()) # print only all keys
print(dic.values()) # print only all values 
# iterate through the dictionary to access elements
for key in dic.keys():  # for keys
    print(key)  
for value in dic.values():  # for values
    print(value) 
for item in dic.items():
    print(item) 
"""

# methods in dictionaries 

std1 = {"name":"Adeel", "Marks": 60 , "is_passed":True} 
std2 = {"name2":"Ahmad", "Marks2": 30 , "is_passed2":True} 
"""
std1.update(std2) # if any key has the same name it will overwrite that 
std1.clear() # clear all the values from dictionary
std1.pop("Marks") # it removes the specific key-value pair from the dictionary
std1.popitem() # it removes the last key value pair from the dictionary
del std1 # deletes the dictionary 
del std1["is_passed"] # deletes the specific key-value from the dictionary 
print(std1["is_passed"]) # to print specific item from the dictionary and will returns error if not found
print(std1.get("name")) #to print specific item from the dictionary and will returns "None" if not found
std1["is_eliible"] = True # adds another item to the dictionary 
list_std = list(std1) # converts dictionary's keys into the list 
list_std = list(std1.values()) # converts dictionary's values into the list 
list_std = list(std1.items()) # converts dictionary's values into the list 

numbers = {1:"adeel",3:"hamza",2:"ali"}
new_std = sorted(numbers)
new_std = list(numbers)
if 2 in new_std:
    print("2 is available") # after converting into list we can find any number in list
print(new_std)

# looping techniques in dictionaries
students = {"Adeel":"Lahore","Bahawal":"Karachi","Jamshaid":"Islamabad"}

for key,value in students.items(): # to get full items (keys, values)
    print(key,"is living in",value) 
for key in students.keys(): # to get keys
    print(key) 
for value in students.values(): # to get values
    print(value) 

# also we have enumate function to for looping through the data types
# for dictionaries
for key,value in enumerate(students.items()):
    print(key,value) 
    
# for lists

student_list = ["Adeel","Bahawal","Jamshaid"] 

for index in enumerate(student_list):
    print(index) 

# if we have to iterate more than one lists at the same time, we can use zip function

questions = ["what is your name: ","What is your Age: ","Which is your city: "]
answers = ["My name is Adeel",30,"Faisalabad"]

for q,a in zip(questions, answers):
    print(q,a) 
    
""" 