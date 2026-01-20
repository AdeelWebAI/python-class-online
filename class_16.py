# sets in python 
# sets are the unordered collection of data in python which don't allow the duplicate values in it.
"""
s = {1,2,3,4,5,4,3,2,4,5,6}
print(s)  # output {1, 2, 3, 4, 5, 6}

# to make an empty set we use 
s = {} # empty dectionary
s = set() # empty set 
s = set([1,2,3,4,5,3,4,5,2,11])
print(s) 

# how to access the sets

for value in s:
    print(value) 
# methods of sets

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

# union and intersectoin for sets

s3 = s1.union(s2) # union of two sets
s4 = s1.intersection(s2)
print(s3) 
print(s4) 

# capitals1 = {"Lahore","Karachi","Queta"} 
# capitals2 = {"Karachi", "Muzafarabad","Islamabad"}
# capitals1.update(capitals2) # update the existing set and add other set in it

# capitals1.intersection_update(capitals2) # update with intersection of two sets

# print(capitals1) 

#symmetric difference
# the values which are not common 

# print(capitals2.symmetric_difference(capitals1)) 

# difference like  (a - b)
# print(capitals1.difference(capitals2))  

"""
capitals1 = {"Islamabad","Karachi","Karachi", "Muzafarabad"}  
capitals2 = {"Karachi", "Muzafarabad","Islamabad"}

# methods for manipulation
# iddisjoint: determine that if they have any common elements # output (True or False)

# print(capitals1.isdisjoint(capitals2))

# issubset: determines that either all values of capitals1 exists in capitals2 

print(capitals1.issubset(capitals2)) 

# issuperset: determines that either all values of capitals2 exists in capitals1 

print(capitals2.issuperset(capitals1)) 

capitals1.add("Faisalabad") # adds an element 
# capitals1.remove("Faisalabad") # removes an element but if does't found it raises error
# capitals1.discard("Faisalabad")# also removes an element but don't raise any error if not found
capitals1.pop() # it pops any random value from the set
# del capitals1 # it deletes the enire set

# capitals1.clear() # clears the whole set

print(capitals1) 
 # if you want to check either a value exists in the set or not you can apply if condition like
 
if "Faisalabad" in capitals1:
    print("Faisalabad is in the Capitals list")
else:
    print("Faisalabad is not in the list of sets") 