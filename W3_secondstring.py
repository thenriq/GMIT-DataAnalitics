string = str(input("Type a string: "))

size = (len(string)) # counting the number of character on string

print(string[-1:-size:-2]) # printing each second string character starting by the last one
