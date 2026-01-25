# os module in python 
 # os moudule is used to handle operating sysems operations in python
 
import os
"""
print(os.getcwd()) # shows the current workng directory 

if (not os.path.exists("assets")):
    os.mkdir("assets")  # ignores condition if folder already exists

for i in range(1,10): 
    os.mkdir(f"assets/folder{i}") # make 10 folders inside assets folder in bulk 
    

for i in range(1,10):
    os.rename(f"assets/folder{i}", f"assets/folder {i}" ) # rename the folders in bulk

print(os.listdir()) # shows the current directories files in bulk
for i in os.listdir():  # shows the same thing in sequence 
    print(i) 
os.remove("sample.py") # deletes files like sample.py (not folers)
os.removedirs("assets") # deletes the empty folder 
for i in range(1,10): 
    os.removedirs(f"assets/folder {i}") # do the same in bulk
""" 