#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    sum = 0
    for j in unique:
        sum += j
    return (sum)
