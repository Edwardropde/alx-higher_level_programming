#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """Replace element in copied list at a certain function."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    temp = [x for x in my_list]
    temp[idx] = element
    return (temp)
