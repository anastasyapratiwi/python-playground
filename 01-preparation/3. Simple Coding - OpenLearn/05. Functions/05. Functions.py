"""
Simple Coding - OpenLearn
Chapter 05. Functions

Instructor:
Michel Wermelinger
Faculty of Mathematics, Computing and Technology
Open University
"""

# The sum function
items = [4.35, 2, 19.95, 22.70, 5]
expenses = sum(items)
print("Food and drinks:"), expenses

# The length function
items = [4.35, 2, 19.95, 22.70, 5]
expenses = len(items)
print("Food and drinks:"), expenses

# -- 5.1 The input function --
# a. Input string
name = input("Tasya")
print("Nice to meet you,"), name

# b. Input number
year = input(2001)
print("Your age is"), 2026 - year

# -- 5.2 Conversion function --
# - Example -
answer = input("In what year were you born?")
year = int(2001)
print("Your age is"), 2026 - year

# -- Activity 8 --
expenses = 54
answer = input("How many people?")
people = int(answer)
if people >= 15:
  percentage = 0.15
elif people > 6:
  percentage = 0.10
else:
  percentage = 0
tip = expenses * percentage
bill = expenses + tip
print("Total bill:"), bill

# -- Tips from Mr. Wermelinger --
"""
1. Good programmers don’t just write code, they write readable code.
2. Code always changes to accommodate further customer requests.
3. Using comments and descriptive names for variables and functions helps making code readable.
"""
