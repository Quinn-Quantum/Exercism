"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_one, list_two):
    list_one_check = (str(list_one).strip("[]") + ",")
    list_two_check = (str(list_two).strip("[]") + ",")
    
    if list_one_check == list_two_check:
        return EQUAL
        
    elif list_two_check in list_one_check:
        return SUPERLIST
        
    elif list_one_check in list_two_check:
        return SUBLIST
    
    else:
        return UNEQUAL
