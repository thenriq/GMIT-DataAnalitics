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




******************************************************************************************
|                                                                                        |
| ATTENTION: The functions below has been moved to a separated file called SquaresGMIT.py |
|                                                                                        |
******************************************************************************************

import math

def squarenumber(number):
    result = math.sqrt(number)
    return result
    

def NewtonSquare(number_given,limit): # function definitions
    attempt = number_given # number to have its square root calculated will work as first attempt to root approximation
    difference = 999999 # A very larger number was assigned to difference to guarantee we can calculate square root for very higher numbers
    count = 0 # this will be used to attempts counting - just to inform user
    while difference > limit:
        newattempt = attempt  - ((attempt ** 2 - number_given) / (2 * attempt)) # here is the Newton Formula working
        difference =  attempt - newattempt
        
        #if difference < 0: # difference value must be always a positive value
        #    difference *= -1
        attempt = newattempt # attempt will always feed Newton function - this will be what function will return in the end
        count = count + 1
    print("Square root calculated in",count,"attempts")
    return attempt
"""
from SquaresGMIT import NewtonSquare # separated function from main program

rootsquare = float(input("Please enter a positive number: "))
approx = float(input("Please type an approximation value (like 0.001 as example): ")) # this is needed because newton's formula calcules square root by approximation

# printing function below calls NewtonSquare funcion, which gets its parameter from variables "rootsquare" and "approx", informed by user
print("The square root of",rootsquare,"is approx %.1f"%round((NewtonSquare(rootsquare,approx)),1))  
# Also, a rounding method has been used for a better result presentation (rounding it to 1 number after comma)