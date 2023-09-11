#!/usr/bin/python3
"""Define a function that returns True if the object is instance of class"""

def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or False
    """
    if type(obj) == a_class:
        return True
    return False
