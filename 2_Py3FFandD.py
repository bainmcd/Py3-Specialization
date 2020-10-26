# This module is a compilation of items
# I need to know for Python 3 Functions, Files, and Dictionaries
# course

##week 1

file_obj = open("StringFileName", "mode")   #returns a open file obj

#can iterate thu each line without reading anything by
for line in file_obj:
    #do something to or with this line

#other methods/functions for txt files
lines = file_obj.readlines()    #returns a list of all the lines
fileString = file_obj.read()    #returns a string of all the file's chars

file_obj.write(varToWrite + "\n")   #varToWrite has to be same type for file
                                #req to include '\n' (newline) chars
                                #the file needs to be openned in the correct mode


file_obj.close()        #need to remember to close the file to clean up

#we can us the following 'with' statement to do file operations
with open("StringFileName", 'r') as file_obj:
    #do some file manip or reading
    #other file stuff in this block
#when the 'with' statement's block is done the close() method is done for you!
    
# here is an example of reading in a .csv file to process

fileconnection = open("olympics.csv", 'r')  #open file for reading
lines = fileconnection.readlines()  #read in all the lines in the file
header = lines[0]
field_names = header.strip().split(',') #make a list of the header fields
print(field_names)
for row in lines[1:]:       #now iterate thru the rest iof the lines doing something
    vals = row.strip().split(',')
    if vals[5] != "NA":
        print("{}: {}; {}".format(
                vals[0],
                vals[4],
                vals[5]))
# an example of writing to a .csv

olympians = [("John Aalberg", 31, "Cross Country Skiing"),
            ("Minna Maarit Aalto", 30, "Sailing"),
            ("Win Valdemar Aaltonen", 54, "Art Competitions"),
            ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv","w")  #open file in the write mode
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows: 'using the format string method, implicit type conversion
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)   #note: you can use ",".join([vars]) if
    outfile.write('\n')         # all the fields contain strings, type conversion
outfile.close()                 # is a problem though

##WEEK2 dictionaries and dictionary accummulation

## example of finding the maximum key value

sally = "sally sells sea shells by the sea shore"
characters = {}
maxk = ""           #this type will have to match the dict key type
for c in sally:
    if c not in characters: #build the dict
        characters[c] = 0
        
    characters[c] = characters[c] + 1
    
    if maxk == "":      # initialize the max key
        maxk = c
    elif characters[c] > characters[maxk]: #track the max value's key
        maxk = c

## example of  finding the minimum key value

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {}
mink = ""       #this type will have to be whatever type the dict keys are
for c in placement:
    if c not in d:  #build the dict
        d[c] = 0
    d[c] = d[c] + 1
    if mink == "":#initialize the min key
        mink = c
    elif d[c] < d[mink]:    #track the min value
            mink = c
 print(mink)   

##week3 Functions and Tuples
##week4 More Iteration and Advanced functions
 
## Lambda functions
 y = (lambda x: -x)     # an anonymous function that has param:funt spec
            
## Equivelent for loop vs while loop
 list1 = [8, 3, 4, 5, 6, 7, 9]
 
 tot = 0
 for elem in list1:
     tot = tot + elem
     
 idx = 0
 accum = 0
 while idx < len(list1):        # can use break to end while loop
     accum = accum + list1[idx] # or can use continue to start next iteration
     idx += 1
print(accum)

## The 'Listener Loop'

theSum = 0
x = -1
while (x != 0):         # In this case listening for an input from the user
    x = int(input("next number to add up (enter 0 if no more numbers): "))
    theSum = theSum + x

print(theSum)

##week5 Sorting



