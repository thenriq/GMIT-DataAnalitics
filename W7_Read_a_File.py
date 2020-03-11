# Thiago Lima


def readfile(filename,character):
    f = open(filename,'r')
    count =0

    
    for line in f:
        for word in line.split():
            for letter in list(word):
                if (letter == character):
                    count = count + 1

    return count
    

filename = str(input("Type the file name: "))
character = str(input("Which character are you looking for? "))

print('Found', (readfile(filename,character)), 'occurrences of ',"'",character,"'" 'character')
            


#f = open('read-a-file.py','r')

#with open('.gitignore','r') as f:
#    print(f.read())
   #- for line in f:
   #-     print (line)
        #print(f.readline())
    #for line in f:
    #    print(line,end = '')



#print(f.read())
#print(f.readline(),end = '')
"""
letterCounter = 0
for line in f:
    for word in line.split():
        for letter in list(word):
            letterCounter[letter]+=1
print(letterCounter)

    

#print(f.read(205))

#print("This is the end")

#f.close()
"""