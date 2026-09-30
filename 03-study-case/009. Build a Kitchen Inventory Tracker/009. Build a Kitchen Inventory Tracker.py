"""
Python Certification freeCodeCamp
Chapter: Python Basics
Subchapter: Build a Kitchen Inventory Tracker (Workshop)
"""

# -- Step 1 --
available_eggs = 1
available_flour = 2
available_sugar = 3

# -- Step 2 --
def check_kitchen_stock():
    pass

# -- Step 3 --
def check_kitchen_stock():
    total_items = available_eggs + available_flour + available_sugar
    return sum(total_items)

# -- Step 4 --
def check_kitchen_stock():
    total_items = available_eggs + available_flour + available_sugar
    print(f'The kitchen has {total_items} total items:')
    print(f'- {available_eggs} eggs')
    print(f'- {available_flour} flour')
    print(f'- {available_sugar} sugar')

# -- Step 5 --
check_kitchen_stock()

# -- Step 6 --
def use_eggs(available_eggs, eggs_to_use):
    pass

# -- Step 7 --
def use_eggs(available_eggs, eggs_to_use):
    if eggs_to_use > available_eggs:
        print("The kitchen does not have enough eggs.")

# -- Step 8 --
def use_eggs(available_eggs, eggs_to_use):
    if eggs_to_use > available_eggs:
        print('The kitchen does not have enough eggs.')
        return(available_eggs) 

# -- Step 9 --
def use_eggs(available_eggs, eggs_to_use):
    if eggs_to_use > available_eggs:
        print('The kitchen does not have enough eggs.')
        return available_eggs

    print(f'{eggs_to_use} egg(s) used out of {available_eggs} available.')
    return available_eggs - eggs_to_use 

# -- Step 10 --
use_eggs(available_eggs, 1)

# -- Step 11 --
print(available_eggs)

# -- Step 12 --
def make_fried_egg(available_eggs):
    pass

# -- Step 13 --
def make_fried_egg(available_eggs):
    has_enough_eggs = available_eggs >= 1

# -- Step 14 --
def make_fried_egg(available_eggs):
    has_enough_eggs = available_eggs >= 1

    if has_enough_eggs:
        available_eggs = use_eggs(available_eggs, 1)
        print("Made a fried egg. Yummy!")
    else:
        print("Could not make a fried egg. Not enough eggs!")
