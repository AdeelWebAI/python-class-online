#------------ Operators----------------

# Arithmetic operators



# | Operator | Description    | Example                     | Result |
# | `+`      | Addition       | `a + b`                     | `13`   |
# | `-`      | Subtraction    | `a - b`                     | `7`    |
# | `*`      | Multiplication | `a * b`                     | `30`   |
# | `/`      | Division       | `a / b`                     | `3.33` |
# | `//`     | Floor Division | `a // b`                    | `3`    |
# | `%`      | Modulus        | `a % b`                     | `1`    |
# | `**`     | Exponentiation | `a ** b`                    | `1000` |

x = 10
y = 3

# print(x//y)

# print(x % y)




#  Comparison Operators


# | Operator | Description           | Example (`a = 10`, `b = 3`) | Result  |
# | `==`     | Equal to              | `a == b`                    | `False` |
# | `!=`     | Not equal to          | `a != b`                    | `True`  |
# | `>`      | Greater than          | `a > b`                     | `True`  |
# | `<`      | Less than             | `a < b`                     | `False` |
# | `>=`     | Greater than or equal | `a >= b`                    | `True`  |
# | `<=`     | Less than or equal    | `a <= b`                    | `False` |

# x = 10
# y = 3

# if x !=  y:
#     print(" equal ")
    
# else:
#     print("not equal")


# x = 10
# y = 3

# if x <=  y:
#     print(" equal ")
    
# else:
#     print("not equal")




#  Logical operators


# | Operator | Description           | Example          | Result  |
# | `and`    | True if both are True | `True and False` | `False` |
# | `or`     | True if one is True   | `True or False`  | `True`  |
# | `not`    | Inverts the result    | `not True`       | `False` |

# x = 10
# y = 20
# z = 30

# print( x < y or y > z or x > z and x > y )    # output is "True"

# example of not operator

# x = 10
# y = 20

# print(not (x > y))   # True


#  Assignment Operators:

# | Operator | Description             | Example   | Equivalent To |
# | `=`      | Assign                  | `a = 5`   | -             |
# | `+=`     | Add and assign          | `a += 3`  | `a = a + 3`   |
# | `-=`     | Subtract and assign     | `a -= 2`  | `a = a - 2`   |
# | `*=`     | Multiply and assign     | `a *= 4`  | `a = a * 4`   |
# | `/=`     | Divide and assign       | `a /= 2`  | `a = a / 2`   |
# | `//=`    | Floor divide and assign | `a //= 3` | `a = a // 3`  |
# | `%=`     | Modulus and assign      | `a %= 2`  | `a = a % 2`   |
# | `**=`    | Power and assign        | `a **= 2` | `a = a ** 2`  |

# x = 10  # Assigned value

# # x = x + 1
# x **= 3
# print(x) 