"""
Python Certification freeCodeCamp
Chapter: Python Basics
Subchapter: Numbers and Mathematical Operations
"""

# -- A. How Do You Work With Integers and Floating Point Numbers? --
# -- 1. With Integers --
# Example Code
my_int_1 = 56
my_int_2 = -4
print(type(my_int_1)) # <class 'int'>
print(type(my_int_2)) # <class 'int'>

# - a. Addition operation with integers -
my_int_1 = 56
my_int_2 = 12
sum_ints = my_int_1 + my_int_2
print('Integer Addition:', sum_ints) # Integer Addition: 68

# - b. Substraction with integers -
my_int_1 = 56
my_int_2 = 12

# Substraction
diff_ints = my_int_1 - my_int_2
print('Integer Substraction:', diff_ints) # Integer Substraction: 44

# - c. Multiplication operation with integers -
my_int_1 = 12
my_int_2 = 4

# Multiplication
product_ints = my_int_1 * my_int_2
print('Integer Multiplication:', product_ints) # Integer Multiplication: 48

# - d. Division operation with integers -
my_int_1 = 56
my_int_2 = 12

# Division
div_ints = my_int_1 / my_int_2
print('Division:', div_ints) # Division: 4.666666666666667

# -- 2. With Floats --
# - a. Addition -
my_float_1 = 5.4
my_float_2 = 12.0

float_addition = my_float_1 + my_float_2
print('Float Addition: ', float_addition) # Float Addition: 17.4

# - b. Substraction -
my_float_1 = 5.4
my_float_2 = 12.0

float_substraction = my_float_2 - my_float_1
print('Float Substraction: ', float_substraction) # Float Substraction: 6.6

# - c. Multiplication -
my_float_1 = 5.4
my_float_2 = 12.0

float_multiplication = my_float_2 * my_float_1
print('Float Multiplication: ', float_multiplication) # Float Multiplication: 64.80000000000001

# - d. Division -
my_float_1 = 5.4
my_float_2 = 12.0

float_division = my_float_2 / my_float_1
print('Float Division: ', float_division) # Float Division: 2.222222222222222

# - e. Add an integer and a float (Result: a float) --
my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float) # 61.4
print(type(sum_int_and_float)) # <class 'float'>

# -- 3. More complex arithmetic calculations --
# - a. Modulo operator (%) -
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print('Integer Modulo: ', mod_ints) # Integer Modulo: 8
print('Float Modulo: ', mod_floats) # Float Modulo: 1.1999999999999993

# - b. Floor division (//) -
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division: ', floor_div_ints) # Integer Floor Division: 4
print('Float Floor Division: ', floor_div_floats) # Float Floor Division: 2.0

# - c. Exponentiation (**) -
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation: ', exp_ints) # Integer Exponentiation: 951166013805414055936
print('Float Exponentiation: ', exp_floats) # Float Exponentiation: 614787626.1765089

# -- 4. Built-in functions --
# - a. float() -
my_int_1 = 56
my_float_1 = float(my_int_1)

print(my_float_1) # 56.0
print(type(my_float_1)) # <class 'float'>

# - b. int() -
my_float = 12.92563
my_int = int(my_float)

print(my_int) # 12
print(type(my_int)) # <class 'int'>

# - Example -
my_str_int = '45'
my_str_float = '7.8'
converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int)) # 45 <class 'int'>
print(converted_float, type(converted_float)) # 7.8 <class 'float'>

# -- 5. Other methods --
# - a. round() -
my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1) # 5
print(rounded_int_2) # 4.3

# - b. abs() -
num = -15

absolute_value = abs(num)
print(absolute_value) # 15

# - c. pow() -
result_1 = pow(2, 3) # Equivalent to 2 ** 3
print(result_1) # 8

result_2 = pow(2, 3, 5) # (2 ** 3) % 5
print(result_2) # 3
