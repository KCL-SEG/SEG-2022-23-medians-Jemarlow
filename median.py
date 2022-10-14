import math

"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

length = numbers.__len__()
i = math.ceil(length / 2) - 1;

if (length % 2 == 0): # even
    m = (numbers[i] + numbers[i + 1]) / 2 # calc mean of middle two numbers
else: # odd
    m = numbers[i] # simply get middle number

print(m)