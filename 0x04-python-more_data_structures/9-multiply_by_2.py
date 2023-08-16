#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    keylist = list(new.keys())
    for j in keylist:
        new[j] *= 2
    return (new)
