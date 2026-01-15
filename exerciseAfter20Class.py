# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the last letter and append it at the start
# now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# your programe should ask the word that you want to code or decode.

import random
import string

a = input("Input a word that you want to encrypt: ")
print(f"you the word {a}") 

b = list(a)
c= b.pop()
b.insert(0,c)
# print(b) 
characters = string.ascii_letters # it will include a-z and A-Z characters

for i in range(3):
    rand_chars = random.choice(characters)
    b.insert(0,rand_chars)
    b.insert(len(b),rand_chars)
c = "".join(b)
print(c)  # here our word is encrypted here we go.....

# when it goes another side it will be decoded by this code.

d = list(c)

for i in range(3):
    d.pop(0)   # removes first word
    d.pop()   # removes last word

# also we can use slicing 
# d = c[3:-3] # removes 3 3 words from start and end.
d.append(d.pop(0)) # remove the first character and append it to the last of the word 
e= "".join(d)
print(e) 
