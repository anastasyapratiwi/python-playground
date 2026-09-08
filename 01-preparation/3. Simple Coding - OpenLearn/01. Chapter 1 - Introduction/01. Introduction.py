"""
Simple Coding - OpenLearn
Chapter 01. Introduction

Michel Wermelinger
Faculty of Mathematics, Computing and Technology
Open University
"""

# Example 1
result = 3 + 7
print("The sum of 3 and 7 is:"), result

# Tweaking 1
result = 3 + 2
print("The sum of 3 and 2 is:"), result

# Example 2
expenses = 54
people = 7
if people > 6:
    percentage = 0.10
else:
    percentage = 0
tip = expenses * percentage
bill = expenses * tip
print("Total Bill:"), bill
