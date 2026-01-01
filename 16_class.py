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
"""
capitals1 = {"Lahore","Karachi","Queta"} 
capitals2 = {"Karachi", "Muzafarabad","Islamabad"}
# capitals1.update(capitals2) # update the existing set and add other set in it

capitals1.intersection_update(capitals2) # update with intersection of two sets

print(capitals1) 
