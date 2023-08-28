#!/usr/bin/python3

def magic_calculation(a, b):
    ret = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception('Too far')
            ret += (a ** b) / x
        except:
            ret = b + a
            break
        return (ret)
