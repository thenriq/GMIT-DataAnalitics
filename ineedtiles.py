# This program calculates how many tiles you will need
# when tiling a wall or floor (in m2)).
# Project available on GIT
length = int(input("Enter room length: "))
width = int(input("Enter room width: "))

area = length * width

needed = area * 1.05

print("You need ",needed, "tiles in metres squared.")
