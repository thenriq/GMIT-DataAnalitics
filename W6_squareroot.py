# Thiago Lima
# Calculating square root of a number and outputing an approximation of its square root.

"""
Weekly task 6

Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. You should create a function called sqrt that does this.

$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.
"""

import math

def squarenumber(number):
    result = math.sqrt(number)
    return result

posnumber = float(input("Please enter a positive number: "))

print("The square root of",posnumber,"is approx.%.1f"%round((squarenumber(posnumber)),1))
#"{0:.2f}".format(a))