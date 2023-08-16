#!/usr/bin/python3
def number_keys(a_dictionary):
    numkeys = 0
    keylist = list(a_dictionary.keys())
    for j in keylist:
        numkeys += 1
    return (numkeys)
