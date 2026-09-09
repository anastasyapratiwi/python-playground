"""
Simple Coding - OpenLearn
Chapter 06. Iteration (part 2)

Instructor:
Michel Wermelinger
Faculty of Mathematics, Computing and Technology
Open University
"""

# - Example -
expenses = 0
while True:
  answer = input("Price of ordered item?")
  if answer == "stop":
    break
  else:
    price = float(answer)
    expenses = expenses + price
print("Total of orders:"), expenses

# -- Activity 9 --
prices = []  # Create an empty list to store all the item prices

# Step 1: Input all the prices first
while True:
    answer = input("Price of ordered item? (or type 'stop'): ")
    if answer.lower() == "stop":
        break
    
    price = float(answer)
    prices.append(price)  # Add the price to our list

# Check if any items were actually ordered before moving on
if len(prices) > 0:
    # Step 2: Calculate the subtotal of all food items
    subtotal = sum(prices)
    
    # Step 3: Input the number of people later
    answer = input("How many people? ")
    people = int(answer)
    
    # Step 4: Determine the tip percentage based on total guests
    if people >= 15:
        percentage = 0.15
    elif people > 6:
        percentage = 0.10
    else:
        percentage = 0
        
    # Step 5: Calculate final tax and tips based on the entire meal
    tip = subtotal * percentage
    vat = subtotal * 0.20
    total_expenses = subtotal + tip + vat

    # Display the final bill breakdown
    print(f"\n--- Final Bill ---")
    print(f"Subtotal:       {subtotal:.2f}")
    print(f"Tip ({percentage*100:.0f}%):     {tip:.2f}")
    print(f"VAT (20%):      {vat:.2f}")
    print(f"Total Bill:     {total_expenses:.2f}")
else:
    print("No items were entered.")

# -- 6.1 The oldest algorithm --
# -- Activity 10 --
# Euclid's greatest common divisor algorithm

# ask user for an integer greater than zero
# store it in n
n = int(input("Enter an integer greater than zero for n: "))
m = int(input("Enter an integer greater than zero for m: "))

# while n and m are different:
while n != m:
  if n > m:
    n = n - m
  else:
    m = m - n
print("Their greatest common divisor is"), n

# ask user for an integer greater than zero
# store it in m
m = int(input("Enter an integer greater than zero for m: "))
n = int(input("Enter an integer greater than zero for n: "))

# while n and m are different:
while n != m:
  if m > n:
    m = m - n
  else:
    n = n - m
print("Their greatest common divisor is"), m

# -- For my Statement of participation from OpenLearn (part of Open University), check README.md. --
# -- Thank you. --
