"""
Simple Coding - OpenLearn
Chapter 03. Selection

Instructor:
Michel Wermelinger
Faculty of Mathematics, Computing and Technology
Open University
"""

# -- 1. Developing software for a restaurant --
expenses = 54
people = 7
if people > 6:
  percentage = 0.10
else:
  percentage = 0

tip = expenses * percentage
bill = expenses + tip
print("Total bill:"), bill

# -- Activity 3 --
expenses = 54
people = 6
if people > 6:
  percentage = 0.10
else:
  percentage = 0

tip = expenses * percentage
bill = expenses + tip
print("Total bill:"), bill

# -- 3.1 And now for something not completely different --
# -- Activity 4 --
# a. For more than 6 people
expenses = 54
people = 9
if people > 6:
  rate = 0.10
else:
  rate = 0

tip = expenses * rate
bill = expenses + tip
print("Total bill:"), bill

# b. For 6 people
expenses = 54
people = 6
if people > 6:
  rate = 0.10
else:
  rate = 0

tip = expenses * rate
bill = expenses + tip
print("Total bill:"), bill

#  c. For less than 6 people
expenses = 54
people = 2
if people > 6:
  rate = 0.10
else:
  rate = 0

tip = expenses * rate
bill = expenses + tip
print("Total bill:"), bill

# -- Addition: Tip of 15% for groups of at least 15 people --
# -- Activity 5 --
# - a. For 6 people -
expenses = 54
people = 6
if people >= 15:
  percentage = 0.15
elif people > 6:
    percentage = 0.10
else:
  percentage = 0

tip = expenses * percentage
bill = expenses + tip
print("Total bill:"), bill

# - b. For 7 people -
expenses = 54
people = 7
if people >= 15:
  percentage = 0.15
elif people > 6:
    percentage = 0.10
else:
  percentage = 0

tip = expenses * percentage
bill = expenses + tip
print("Total bill:"), bill

# - c. For 14 people -
expenses = 54
people = 14
if people >= 15:
  percentage = 0.15
elif people > 6:
    percentage = 0.10
else:
  percentage = 0

tip = expenses * percentage
bill = expenses + tip
print("Total bill:"), bill

# - d. For 15 people: -
expenses = 54
people = 15
if people >= 15:
  percentage = 0.15
elif people > 6:
    percentage = 0.10
else:
  percentage = 0

tip = expenses * percentage
bill = expenses + tip
print("Total bill:"), bill

# -- Activity 6 --


# -- Tips from Mr. Wermelinger --
# 1. Usually there are many ways to solve the same problem
# 2. The order in which we write the conditions is important, because the computer checks them from top to bottom and executes only one block, for the first condition that is true. The else block has no condition, so it’s a ‘catch all’ in case no condition is true.
# 3. 
