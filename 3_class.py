# string methods
# First of all keep in mind that strings are 'immutable'. Means directly you can't change the strings. Every string method that you will apply that will make a new string using that method.

a = "It is a string"
# print(len(a)) # length of a string
# print(a.upper()) # upper case
# print(a.lower()) # lower case
# print(a.rstrip("@!")) # strip the trailing characters from end
# print(a.replace("Python","zero")) # replace characters or words
# print(a.split(" ")) # it converts the string into a list
# print(a.capitalize()) # this makes first character of string capitalize
# print(a.center(20)) # it addes the number of spaces before the string
# print(a.count("It")) # count the words or character in string

a = "Welcome to the class of python"
# print(a.endswith("python")) # determine that either string ends with the word or not
# print(a.startswith("Welcome")) # determine that either string starts with the word or not
# print(a.endswith("class", 0,20 )) # determine that either string ends with a specific slice of string index
# print(a.find("o")) # finds the index of first occurance of a word or character and return -1 if not found
# print(a.index("asdf")) # same as find method but it returns an error if not found
a = "Welcome to our class"
# print(a.isalnum()) # checks that either the string is alpha numeric or not (a-z,A-Z,0-9) no spaces included
# print(a.isalpha()) # check that string is alphabetical or not
# print(a.isnumeric()) # check that string is numeric or not
# print(a.islower()) # check that string is lower case or not
# print(a.isupper()) # check that string is upper case or not
# print(a.isprintable()) # check that string is printable or not
# print(a.isspace()) # check that string is printable or not
# print(a.istitle()) # check that string is title or not means the first character of each word of the string is capital or not
# print(a.swapcase()) # change the case of every character
# print(a.title()) # change the string to title , means it capitalize the first character of every character