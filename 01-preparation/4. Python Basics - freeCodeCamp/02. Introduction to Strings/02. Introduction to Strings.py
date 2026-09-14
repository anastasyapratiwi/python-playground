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
print(my_str[-2]) # 1

# Assign a different string to a variable (immutable)
greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

# Don't direct modification of a string
greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment

