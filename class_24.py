# File Handling in python 
"""
file = open("file1.txt","r") # "r" mode opens the file
# open("file1.txt","w") # "w" write mode writes file if not exist and if already have itwill overwrite it.
file.close() # closes opened file 

file = open("test.txt", "w")
file.write("Hello Python")
file.close()

file = open("test.txt", "r")
print(file.read())
file.close() 

file = open("text.txt","a") # opens in append mode 
file.write("\n hello python again ")  # writes data in file

file = open("newfile.txt", "x") # openn in create mode. Error if already exists
file.write("New file created")
file.close()

file = open("test.txt", "r+") # opens in write and read mode
print(file.read())
file.write("\nAdded text")
file.close() 

# f = open("file1.txt","r") 
# manual method
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline() 
# print(line1)
# print(line2)
# print(line3)
# write lines methods in file handling

# with readline() method
f = open("file1.txt", "r")

line = f.readline()

while line:
    print(line)
    line = f.readline()

# Write lines method

w = open("file3.txt","w")
countries = ["pakistan\n","india\n","Nepal\n","Bengaldesh\n","Sri Lanka"] 
# or for new line we can can run loop because writelines() method don't goes on new line
w.writelines(countries)
"""
    
# seek() , tell() methods in file handling 
f = open("file1.txt", "r")
# if i want to skipp first 20 characters i will seek
f.seek(20)

file = f.read() 

# print(file) 

# tell method: It tell us how many characters we have seeked.

print(f.tell()) 