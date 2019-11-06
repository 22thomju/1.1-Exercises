#!/usr/bin/env python3

# display a welcome message
print("The Area and Perimeter program")
print()

# get input from the user
length = float(input("Please enter the length:\t"))
width = float(input("Please enter the width:\t\t"))

# calculate miles per gallon
ar = length * width
pe = (length * 2) + (width * 2)
            
# format and display the result
print()
print("Area =\t\t" + str(ar))
print("Perimeter =\t" + str(pe))
print()
print("Thanks for using this program!")


