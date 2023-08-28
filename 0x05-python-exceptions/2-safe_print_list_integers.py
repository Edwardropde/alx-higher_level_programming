#!/usr/bin/python

def safe_print_list_integers(my_list=[], x=0):
    r = 0
    try:
        for j in range(0, x):
            try:
                if isinstance(my_list[j], int):
                    print("{:d}".format(my_list[j]), end="")
                    r += 1
            except (ValueError, TypeError):
                pass
    finally:
        print()
    return (r)
