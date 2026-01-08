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
"""
for item in dic.items():
    print(item) 