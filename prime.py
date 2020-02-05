# Thiago Lima
# Check if a number isprime.
# The primes are 2, 3, 5, 7, 11, 13, ...

p = 221 
m = 2
isprime = True

"""
while m < p:
    if p % m == 0:
        isprime = False
        break
    m = m + 1
"""
for m in range(2, p-1):
    if p % m == 0:
        isprime = False
        break
    
if isprime:
    print(p,"is a prime number.")
else:
    print(p, "is not prime.")

print("Thank you for runing my program. ")