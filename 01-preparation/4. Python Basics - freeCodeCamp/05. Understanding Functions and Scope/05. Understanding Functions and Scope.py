"""
Python Certification freeCodeCamp
Chapter: Python Basics
Subchapter: Understanding Functions and Scope
"""

# -- A. How Do Functions Work in Python? --
# -- 1. input() --
name = input('What is your name?') # User types "Kolade" and presses Enter
print('Hello', name) # Output: Hello Kolade

# -- 2. int() --
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0

# -- 3. def --
# - a. Function named "hello" -
def hello():
  print('Hello World')

hello() # Hello World

# - b. Function (sum of two numbers) -
def calculate_sum(a, b):
  print(a + b)

# -- 4. Arguments --
# - a. Call the function -
calculate_sum(3, 1) # 4

# - b. Without the correct number (TypeError) -
calculate_sum()
# TypeError: calculate_sum() missing 2 required positional arguments: 'a' and 'b'

# -- 5. return --
# - a. Without return (None) -
def calculate_sum(a, b):
  print(a + b)

my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None

# - b. With return -
def calculate_sum(a, b):
  return a + b

my_sum = calculate_sum(3, 1)
print(my_sum) # 4

# -- B. What Is Scope in Python and How Does It Work? --
# Example 1 (local and global scope)
tax_rate = 0.1

def calculate_tax(price):
  tax = price * tax_rate
  return tax

print(calculate_tax(50)) # 5.0
print(tax_rate) # 0.1
print(tax) # NameError: name 'tax' is not defined

# Example 2
discount = 0.2

def apply_discount(price):
  amount = price * discount
  return price - amount

# Example 3
def greet():
  message = 'Hello!'
  print(message)

greet()
print(message)
