# This module is a compilation of the items
# I need to know for Python3 Basics course

# Weeks 1 and 2
            #import brings in other modules, from /usr/lib/Python ish
import turtle   #I think part of standard lib, for beginning teaching
import random   #for obvious purposes
#from random import random   #just import the random function from random
                            #module
import math as m #alias the math module as m, then can code m.function()
                 #instead of math.function()

string1 = "This is a string"
strint2 = 'This is also a string with single quotes'
lst1 = [1,2,3,4,5] #a list is contained in [], and can be any type
lst2 = [1, "2", 3.3,[2,4,6],"word"]
tpl = (1,'2',3.3,"word") # a tuple is an immutable collection of various types
                         # it is contained in ()
print(lst1[0:8])    #will print the substring using the slice operator
                    # [n:m], includes n up to but excluding m
                    # [:m], from the start
                    # [n:], from n to the end of string
                    # slices also work with lists and tuples
                    
print(lst1) #print the list


words = string1.split(" ")  #returns a list of items split  using the defined
print(words)                #seperator. if () whitespace is used as seperator

newWords = " ".join(words)  #returns a joined striing using the glue, or seperator
print(type(newWords))       #indicated in preceding the .join

type(string1) #returns a string containing the type of the variable passed in.
len(string1) #returns an int with the length of the string passed in
s = input("User input prompt ") #promt for user input, returns a string

r = list(range(41)) #creates a list of int 0 up to, but not including 41
print(r)


#instantiate a turtle object from turtle module
tur = turtle.Turtle() #new turtle object
wndw = turtle.Screen() #window for tur to do stuff

tur.forward(50) #move tur fwd 50 units method
tur.right(45) #tur turns right 45 degrees method
wndw.exitonclick() #close window method


#Instantiate a random object from the random module
rdm = random.random()
print(rdm)

rdmrng = random.randrange(3,9) #returns an int from 3 up to, but not including 9
print(rdmrng)

# for loop example
iterable = list(range(50)) # empty list to iterate thru
idx = 0  # counting or traversing a sequence, not req
tot = 0  # accumulator pattern, not req
for it in iterable:
    print(idx,str(it),type(it),tot)  #cast it to string, just to show casting
    idx += 1
    tot += idx
                             
# Weeks 3
# Week 4

#List methods check Runestone 9.7 for explanations
mylist = []
mylist.append(5)

print(mylist)

mylist.insert(1, 12)

print(mylist.count(12))

print(mylist.index(3))

mylist.reverse()

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)

##Method 	Parameters 	Result 	        Description
##append 	item 	        mutator 	Adds a new item to the end of a list
##insert 	position, item 	mutator 	Inserts a new item at the position given
##pop 	        none 	        hybrid 	        Removes and returns the last item
##pop 	        position 	hybrid 	        Removes and returns the item at position
##sort 	        none 	        mutator 	Modifies a list to be sorted
##reverse 	none 	        mutator 	Modifies a list to be in reverse order
##index 	item 	        return idx 	Returns the position of first occurrence of item
##count 	item 	        return ct 	Returns the number of occurrences of item
##remove 	item 	        mutator 	Removes the first occurrence of item


# Non-mutating string methods
ss = "Hello, World"
print(ss.upper())

tt = ss.lower()
print(tt)
print(ss)

##Method 	Parameters 	Description
##upper 	none 	        Returns a string in all uppercase
##lower 	none 	        Returns a string in all lowercase
##count 	item 	        Returns the number of occurrences of item
##index 	item 	        Returns the leftmost index where the substring item is found and causes a runtime error if item is not found
##strip 	none 	        Returns a string with the leading and trailing whitespace removed
##replace 	old, new 	Replaces all occurrences of old substring with new
##format 	substitutions   use this to add parameters to strings, and format display

