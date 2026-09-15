"""
Python Certification freeCodeCamp
Chapter: Python Basics
Sub-Chapter: Introduction to Strings
"""

# -- A. What Are Strings and What Is String Immutability? --
# Example code
my_str_1 = 'Hello'
my_str_2 = "World"

# Multi-line string example
my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''

# If the strings contains either single or double quotation marks
# a. Use the opposite kind of quotes
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

# b. Use backlash (\) for the same quotation marks
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""

# in (check if a string contains one or more characters)
my_str = 'Hello world'

print('Hello' in my_str) # True
print('hey' in my_str) # False
print('hi' in my_str) # False
print('e' in my_str) # True
print('f' in my_str) # False

# len(): Get the length of a string
my_str = 'Hello world'
print(len(my_str)) # 11

# []: Access a character by its index
my_str = "Hello world"
print(my_str[0]) # H
print(my_str[6]) # w

# Negative indexing (from the last character)
my_str = 'Hello world'
print(my_str[-1]) # d
print(my_str[-2]) # l

# Assign a different string to a variable (immutable)
greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

# Don't direct modification of a string
greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment

# -- B. What Are String Concatenation and String Interpolation? --
# 1. String Concatenation (+)
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World

# 2. Repeating Strings (*)
sound = 'ha'
repeated_sound = sound * 3
print(repeated_sound) # hahaha

# 3. Concatenating Strings with Numbers
# a. Directly (TypeError)
name = 'John Doe'
age = 26
name_and_age = name + age
print(name_and_age) # TypeError: can only concatenate str (not "int") to str

# b. str(): convert the value into a string
name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26

# c. Concatenation and assignment in one step (+=)
name = 'John Doe'
age = 26

name_and_age = name # Start with the name
name_and_age += str(age) # Append the age as string

print(name_and_age) # John Doe26

# 4. String Interpolation (f-strings)
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15

# -- C. What Is String Slicing and How Does It Work? --
my_str = "Hello world"

print(my_str[0]) # H
print(my_str[6]) # w
print(my_str[-1]) # d

# Basic syntax of String slicing (extract a specific part)
# string[start:stop]

# - 1. Extract characters (separate with a colon) -
my_str = 'Hello world'
print(my_str[1:4]) # ell

# - 2. Omit to default [0] -
# a. Omit the start index
my_str = 'Hello world'
print(my_str[:7]) # Hello w

# b. Omit the stop index
my_str = 'Hello world'
print(my_str[8:])

# Slicing doesn't modify
my_str = 'Hello world'
print(my_str[8:]) # rld
print(my_str) # Hello world

# c. Omit the start and stop indices --> extract the whole string
my_str = 'Hello world'
print(my_str[:]) # Hello world

# - 3. Optional: step parameter -
# string[start:stop:step]

# a. Example (start index 0, stops before 11, and extract every second character)
my_str = 'Hello world'
print(my_str[0:11:2]) # Hlowrd

# b. Reverse a string by setting step to -1, omit both start and stop indices
my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH
