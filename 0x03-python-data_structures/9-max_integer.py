#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    """Finds the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)
    biggest = my_list[0]
    for x in range(len(my_list)):
        if my_list[x] > biggest:
            biggest = my_list[x]
    return (biggest)
