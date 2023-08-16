#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keylist = list(a_dictionary.keys())
    for x in keylist:
        if value == a_dictionary.get(x):
            del a_dictionary[x]
    return (a_dictionary)
