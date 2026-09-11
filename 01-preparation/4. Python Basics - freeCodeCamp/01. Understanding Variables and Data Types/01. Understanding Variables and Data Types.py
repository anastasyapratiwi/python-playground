"""
Python Certification freeCodeCamp
Chapter: Python Basics
Sub-Chapter: Understanding Variables and Data Types
"""

# -- A. How Do You Declare Variables and What Are Naming Conventions to Name Variables? --
# 1. Example to create name and age variables:
name = 'John Doe'
age = 25

# 2. Variable names should be in lowercase, separated by an underscore (snake case)
my_variable_name = 'freeCodeCamp'

# 3. Use descriptive names for variables
user_age = 30

# 4. Avoid using single-letter variable names
x = 56 # What do you mean by x?

# 5. Comments to let you add notes and explanations to your code
# This is a single-line comment
# This is a
# multi-line
# comment

# -- B. How Does the Print Function Work? --
# 1. A common first program display
print('Hello world!') # Hello world!

# 2. Show multiple values or arguments
print('My favorite colors are', 'blue', 'green', 'red')
# Output: My favorite colors are blue green red

# -- C. What Are Common Data Types in Python? --
name = 'John Doe' # Python knows this is a string
age = 25 # Python knows this is an integer

# 1. Assigned a variable to a different type
age = 25
age = 'Twenty-five'

# 2. Integer (whole number without decimals)
my_integer_var = 10
print('Integer:', my_integer_var) # Integer: 10

# 3. Float (number with a decimal point)
my_float_var = 4.50
print('Float:', my_float_var) # Float 4.5

# 4. String (characters enclosed in single or double quotation marks)
my_string_var = 'hello'
print('String:', my_string_var) # String: hello

# 5. Boolean (True or False)
my_boolean_var = True
print('Boolean:', my_boolean_var) # Boolean: True

# -- D. How Do the type() and isinstance() Functions Work? --
# -- 1. type() function --
developer = 'Devin'
print(type(developer)) # <class 'str'> means String

# Error Example
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: type() takes 1 or 3 arguments
"""

# Complete data types
my_integer_var = 10
print(type(my_integer_var)) # <class 'int'>

my_float_var = 4.50
print(type(my_float_var)) # <class 'float'>

my_string_var = 'hello'
print(type(my_string_var)) # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var)) # <class 'bool'>

# -- 2. isinstance() function
# Error when trying to perform mathematical operations
account_balance = '12'
account_balance / 2

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for /: 'str' and 'int'

#  See if the data type is an integer
account_balance = '12'
isinstance(account_balance, int) # False

# Check for multiple types at once
account_balance = 12
isinstance(account_balance, (int, float)) # True
