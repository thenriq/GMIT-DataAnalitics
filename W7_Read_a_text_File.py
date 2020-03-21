# Thiago Lima
# This program ask for a file name (file must be in the same folder), then it asks for a
# desired character to be seek throughout the program and outputs the number of this character occurence


def readfile(filename,character): # function definitions: it asks for a filename and the seek character
    f = open(filename,'r') # user will input file name
    count =0 # this will summarize the number of the seek character
    
    for line in f: #get the line
        #for word in line.split(): # split the line into words
        for letter in list(line): # split the word into characters
            if (letter == character): # compares whether or not each character is equal to the seek character
                count = count + 1 # if character is found, it is summarized with count

    return count # result of this function
    
###############################################################

filename = str(input("Type the file name: "))
character = str(input("Which character are you looking for? "))

# the line below will print and call the funcion "readfile" at the same time
print('Found', (readfile(filename,character)), 'occurrences of ',"'",character,"'" 'character')
            


