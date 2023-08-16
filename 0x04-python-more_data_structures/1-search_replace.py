#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = list(map(lambda y: replace if y == search else y, my_list))
    return (new)
