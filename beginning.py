# writing the first code

print("Hello World")

# creating a shape

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# variables and data types

# creating Variables

character_name = "Prasanth"
character_age = "26"
print("hi myself " + character_name)
print("I am " +character_age+ "years old")
character_name = "kaizoku"
character_age = "30"
print("my goal is to become a data scientist before I cross " +character_age+ " years.")
print("and i also like to be called as " +character_name+ ".")

# String is basically a plain text # three types of basic datatypes, 1. strings, 2. numbers, 3. Booleans.(True and false)

#strings
phrase = "pirate\nking" # \n will make the string mob=ve to next line.
print(phrase)

Luffy = '\"orewa kaizoku oni naru\"' # for double quotes to stay.
print("Luffy says everytime " + Luffy) # + is used to concatenate the strings

#functions

print(Luffy.upper()) #lower,upper,
print(Luffy.isupper()) # to check wether the string is in upper or lower case gives a boolean value.
print(Luffy.upper().isupper()) #combination of functions / gives the value to be True.

print(len(Luffy)) #to find the character length use len.
print(Luffy[1:6]) #grabbing the values using indexing.
print(Luffy.index("kaizoku")) # to find the index value of the string
print(Luffy.replace("kaizoku","Pasanth")) #replacing the string values using the replace function.

#Numbers
print(3+2) #usiing the arithmetic operators.
print(3*(7+2)) #using paranteses to sort the order of operations.
num = 17 #storing numbers in variables
num2 = 7
print(num ** num2) # using the asigned variables and using the arithmetic operations.
print(str(num)) #converting the number to a
print("my favourite number is " +str(num2))

num3 = -5.432
print(abs(num3)) # gives the absolute value.
print(pow(17,7)) # it gives the power of the number
print(max(17,7,3)) # max and min value
print(min(17,7,3))
print(round(-5.43567,3)) #rounding to the nearest decimal fn. the next number determines no of decimal points.

from math import * #importing the math module to use lot more math functions.
print(floor(-5.43567)) # gives the least rounded value so -6
print(ceil(-5.43567)) #gives the highest rounded value so,-5
print(sqrt(17171717171717)) # gives the aquare rot of the number.

#getting input from the users
