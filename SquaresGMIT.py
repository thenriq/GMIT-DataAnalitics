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
        attempt = newattempt # attempt will always feed Newton function - this will be what function will return in the end
        count = count + 1
    print("Square root calculated in",count,"attempts")
    
    return attempt