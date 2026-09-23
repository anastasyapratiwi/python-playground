"""
Python Certification freeCodeCamp
Chapter: Python Basics
Subchapter: Build a Movie Ticket Booking Calculator (Workshop)
"""

# -- Step 1 --
base_price = 15
age = 21

# -- Step 2 --
seat_type = "Gold"
show_time = "Evening"

# -- Step 3 --
if age > 17:
    print("User is eligible to book a ticket")

# -- Step 4 --
if age >= 21:
    print("User is eligible for Evening shows")

# -- Step 5 --
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print("User is not eligible for Evening shows")
  
# -- Step 6 --
is_member = True
is_weekend = False

# -- Step 7 --
discount = 0

# -- Step 8 --
if is_member:
    discount = 3 
    print("User qualifies for membership discount")

# -- Step 9 --
if is_member:
    discount = 3
    print('User qualifies for membership discount')
else:
    print("User does not qualify for membership discount")
print("Discount:", discount)

# -- Step 10 --
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

# -- Step 11 --
is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

# -- Step 12 --
extra_charges = 0
if is_weekend:
    extra_charges = 2
    print("Extra charges will be applied")

# -- Step 13 --
extra_charges = 0
if is_weekend:
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print("No extra charges will be applied")
print("Extra charges:", extra_charges)

# -- Step 14 --
extra_charges = 0
if is_weekend or show_time == "Evening":
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

# -- Step 15 --
if age >= 21:
    print("Ticket booking condition satisfied")
else:
    print("Ticket booking failed due to restrictions")

# -- Step 16 --
if age >= 21 or age >= 18 and show_time != "Evening":
    print('Ticket booking condition satisfied')
else:
    print('Ticket booking failed due to restrictions')

# -- Step 17 --
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')
else:
    print('Ticket booking failed due to restrictions')

# -- Step 18 --
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == "Premium":
        service_charges = 5
else:
    print('Ticket booking failed due to restrictions')

# -- Step 19 --
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    else:
        service_charges = 1    
else:
    print('Ticket booking failed due to restrictions')

# -- Step 20 --
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == "Gold":
        service_charges = 3
    else:
        service_charges = 1
    print("Service charges:", service_charges)
else:
    print('Ticket booking failed due to restrictions')

# -- Step 21 --
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    final_price = base_price + extra_charges + service_charges - discount
    print("Final price of ticket:", final_price)
else:
    print('Ticket booking failed due to restrictions')
