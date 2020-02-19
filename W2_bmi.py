"""
This program calculates somebody's Body Mass Index (BMI)
The inputs are the person's height in centimetres and weight in kilograms. 
The output is their weight divided by their height in metres squared. 

BMI = (weight / (height ** 2)
weight in Kg
height in cm
"""

weight = int(input("Type your WEIGHT: "))
height = int(input("Type hour height in CENTIMETRES: "))

BMI = (weight / ((height / 100) ** 2))

print("Your BMI is: ",BMI)
