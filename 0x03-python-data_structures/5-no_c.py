#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """Removes all characters c and C from a string."""
    temp = [y for y in my_string if y != 'c' and y != 'C']
    return ("".join(temp))
