"""
Simple Coding - OpenLearn
Chapter 02. Sequence
2.1 The art of failure

Instructor:
Michel Wermelinger
Faculty of Mathematics, Computing and Technology
Open University
"""

# -- 1. Activity 1 --
result = 3 + "7"
# Output: type error (adding number to a string)

# -- 2. Activity 2 --
result = 3 + 7
print("The sum of 3 and 7 is:"), "result"
# Output: It won't print the sum number

# Explanation:  "result", "7", result and 7 are different things.
# "result" and "7": string
# result: variable
# 7: number

# The correct code:
result = 3 + 7
print("The sum of 3 and 7 is:"), result

# -- Tips from Mr. Wermelinger
# 1. Learning from mistakes is always helpful
# 2. He encourage to introduce errors and observe what message or output I get
# 3. Don’t forget to reset the program after each error
# 4. It’s best to get used to doing errors on purpose, so no matter how cryptic the error message, I have a clue of what might be wrong when writing my code.
