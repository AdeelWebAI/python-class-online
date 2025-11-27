# Q.1
# my_numbers = [10, 20, 30, 40, 50]

# for i in range(4):
#     my_numbers.insert(i, my_numbers[-1])

# print(my_numbers)

# Q.2

# def compute_square(x):
#     return x * x


# def compute_quad(x):
#     return compute_square(x) * compute_square(None)


# print(compute_quad(4))

# Q.3

# print(1 // 2)
# Q.4

# def raise_power(base, exponent):
#     return base ** exponent


# print(raise_power(exponent=3, 2))
# Q.5

# z = 0
# y = 10
# x = y < z and z > y or y < z and z < y
# print(x)

# Q. 6

# reserved keyword
# continue = 3
# true = 10 

# Q.7

# my_values = [3 * i for i in range(5)]


# def modify_list(values):
#     del values[values[2] // 3]
#     return values


# print(modify_list(my_values))

# Q.8

# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z

# print(x, y, z)

# Q.9

# a = 1
# b = 0
# a = a ^ b
# b = a ^ b
# a = a ^ b

# print(a, b)

# Q.10

# def custom_function(value):
#     if value % 3 == 0:
#         return 1
#     else:
#         return 2
# print(custom_function(custom_function(4)))

# Q.11

# inventory = ['apple', 'banana', 'cherry']
# backup_inventory = inventory
# del backup_inventory[:]

# Q.12

# first_input = input("Enter first number: ")
# second_input = input("Enter second number: ")
# print(second_input + first_input)

# Q.13

# print("a", "b", "c", sep="sep")

# Q.14
# x = 1 // 5 + 1 / 5
# print(x)

# Q.15
# x = float(input())
# y = float(input())
# print(y ** (1 / x))

# Q.16
# dictionary = {'alpha': 'beta', 'gamma': 'alpha', 'beta': 'gamma'}
# value = dictionary['gamma']

# for key in range(len(dictionary)):
#     value = dictionary[value]

# print(value)
# Q.17
# values = [i for i in range(-1, -3, -1)]

# print(values)

# Q.18

# def fun(x, y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y-1)


# print(fun(0, 3))
# Q.19
# i = 0
# while i < i + 2 :
#     i += 1
#     print("*")
# else:
#     print("*")
# Q.19

# my_tuple = (10, 20, 30, 40, 50)
# my_tuple = my_tuple[-3:-1]
# my_tuple = my_tuple[-1]
# print(my_tuple)

# q.20

# dct = {}
# dct['1'] = (1, 2)
# dct['2'] = (2, 1)

# for x in dct.keys():
#     print(dct[x][1], end="")

# Q.21

# matrix = [[x for x in range(3)] for y in range(3)]

# count = 0
# for row in matrix:
#     for element in row:
#         if element % 2 != 0:
#             count += 1
# print(count)

# Q.22
# try:
#     value = input("Enter a value: ")
#     print(int(value)/len(value))
# except ValueError:
#     print("Bad input...")
# except ZeroDivisionError:
#     print("Very bad input...")
# except TypeError:
#     print("Very very bad input...")
# except:
#     print("Booo!")

# Q.23

# try:
#     print(10 / 0)
#     break
# except ZeroDivisionError::
#     print("Zero division error occurred...")
# except (ValueError, TypeError):
#     print("Value or type error occurred..")
# except:
#     print("Unknown error occurred...")

# Q.24
# foo = (1, 2, 3)
# foo.index(0)
# def my_fun(n):
#     s = '+'
#     for i in range(n):
#         s += s
#         yield s

# Q.25
# for x in my_fun(2):
#     print(x, end='')
# Q.26
# class I:
#     def __init__(self):
#         self.s = 'abc'
#         self.i = 0
# Q.27
#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.i == len(self.s):
#             raise StopIteration
#         v = self.s[self.i]
#         self.i += 1
#         return v

# Q.28
# for x in I():
#     print(x, end='')

# Q.29

# def generate_pattern(n):
#     def create_pattern():
#         return '**' * n

#     return create_pattern

# pattern1 = generate_pattern(1)
# pattern2 = generate_pattern(2)
# print(pattern1() + pattern2())

# Q.30

# from datetime import datetime

# datetime_1 = datetime(2019, 11, 27, 11, 27, 22)
# datetime_2 = datetime(2019, 11, 27, 0, 0, 0)

# print(datetime_1 - datetime_2)

# Q.31

import calendar

calendar.setfirstweekday(calendar.FRIDAY)
print(calendar.weekheader(2))
