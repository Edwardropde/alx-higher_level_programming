#!/usr/bin/python3
"""Define object attribute lookup function"""

def lookup(obj):
    """Returns a list of available attributes and methods of an objects"""
    return (dir(obj))
