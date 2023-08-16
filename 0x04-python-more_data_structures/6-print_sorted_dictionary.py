#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    l_ord = list(a_dictionary.keys())
    l_ord.sort()
    for j in l_ord:
        print("{}: {}".format(j, a_dictionary.get(j)))
