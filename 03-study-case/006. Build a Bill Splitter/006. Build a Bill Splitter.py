"""
Python Certification freeCodeCamp
Chapter: Python Basics
Subchapter: Build a Bill Splitter (Workshop)
"""

# -- 1. Step 1 --
running_total = 0

# -- 2. Step 2 --
num_of_friends = 4

# -- 3. Step 3 --
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# -- 4. Step 4 --
running_total += appetizers + main_courses + desserts + drinks
print("Total bill so far:", running_total)

# -- 5. Step 5 --
tip = running_total * 0.25
print("Tip amount:", tip)

# -- Step 6 --
running_total += tip
print("Total with tip:", running_total)

# -- Step 7 --
final_bill = running_total / num_of_friends
print("Bill per person:", final_bill)

# -- Step 8 --
each_pays = round(final_bill, 2)
print("Each person pays:", each_pays)
