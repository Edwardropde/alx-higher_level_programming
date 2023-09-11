#!/usr/bin/python3
"""Define a class and inherited class-checking function"""

def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or inherited of class

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass
    """
    if isinstance(obj, a_class):
        return True
    return False
