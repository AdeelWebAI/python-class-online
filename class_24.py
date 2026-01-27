# File Handling in python 

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

