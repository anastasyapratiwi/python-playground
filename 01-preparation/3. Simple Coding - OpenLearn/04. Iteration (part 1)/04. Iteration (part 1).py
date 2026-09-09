"""
Simple Coding - OpenLearn
Chapter 04. Iteration (part 1)

Instructor:
Michel Wermelinger
Faculty of Mathematics, Computing and Technology
Open University
"""

# -- Example --
# Let the items be a list of the prices of the food and drinks ordered.
items = [4.35, 2, 19.95, 22.70, 5] # same total as before: 54
# Let the expenses be zero.
expenses = 0
# For each item in the items list:
for item in items:
  # Add it to the expenses.
  expenses = expenses + item
# Print the expenses.
print("Food and drinks:"), expenses

# -- Activity 7 --
# - a. Using for loop -
# Let the items be a list of the prices of the food and drinks ordered.
items = [4.35, 2, 19.95, 22.70, 5]
# Set the counter to zero
total_items = 0
# Input the logic with for loop
for item in items:
  total_items +=1 # Adds 1 to the counter
# Print the result
print(f"Total items ordered: {total_items}")

# - b. Using len() -
items = [4.35, 2, 19.95, 22.70, 5]
# Calculate the total of items were ordered
total_items = len(items)
# Print the result
print(f"Total items ordered: {total_items}")
