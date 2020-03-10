"""
Weekly task 4

Write a program that asks the user to input any positive integer and outputs the successive values 
of the following calculation. At each step calculate the next value by taking the current value and, 
if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program 
end if the current value is one.

if number even:
    number / 2
if number odd:
    number * 3 + 1
until number = 1

number = 10
10 / 2 = 5
number = 5
5 x 3 + 1 = 16
number = 16
16 / 2 = 8
number = 8
8 / 2 = 4
number = 4
4 / 2 = 2
number = 2
2 / 2 = 1
number = 1
end

"""
number = int(input("Please type a number: "))

while number != 1:
    
    if (number % 2) == 0: # if number is even, it is divided by 2
        number = number / 2
    else:
        number = number * 3 + 1 #if number is odd, it is multipled by 3 and added 1
    print("Number =",number)
