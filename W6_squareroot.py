# Thiago Lima
# Calculating square root of a number and outputing an approximation of its square root

"""
Weekly task 6

Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. You should create a function called sqrt that does this.

$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.

*********************
*** Newton Method ***
*********************
next_guess = previous_guess  - ((previous_guess**2 - number_given) / (2 * previous_guess))
difference = next_guess - previous_guess

previous_guess = next_guess

if difference < error_limit: end

error limit = 0.000001
number_given = 8
previous_guess = number_given
previous_guess = 8

next_guess1 = previous_guess - ((previous_guess ** 2 - number_given) / (2 * previous_guess))
next_guess1 = 8 - ((8 ** 2 - 8) / (2 * 8))
next_guess1 = 4.5
previous_guess1 = next_guess1
number_given - next_guess1 = 8 - 4.5 = 3.5 (> 0.000001)

next_guess2 = previous_guess1 - ((previous_guess1 ** 2 - number_given ) / (2 * previous_guess1))
next_guess2 = 4.5 - ((4.5 ** 2 - 8) / (2 * 8))
next_guess2 = 3.7343
next_guess3 = next_guess2
next_guess1 - next_guess2 =  0.7657 (> 0.000001) 
continue until error limit < 0.0000001
"""
"""
import math

def squarenumber(number):
    result = math.sqrt(number)
    return result
"""
#posnumber = float(input("Please enter a positive number: "))

def NewtonSquare(number_given,limit):
    attempt = number_given
    difference = 999999
    count = 0
    while difference > limit:
        newattempt = attempt  - ((attempt ** 2 - number_given) / (2 * attempt))
        difference =  newattempt - attempt
        
        if difference < 0:
            difference *= -1
        attempt = newattempt
        count = count + 1
    print("Square root calculated in",count,"attempts")
    return attempt
    

rootsquare = float(input("Please enter a positive number: "))
approx = float(input("Please type an approximation value (like 0.001 as example): "))

print("The square root of",rootsquare,"is approx.",NewtonSquare(rootsquare,approx))
