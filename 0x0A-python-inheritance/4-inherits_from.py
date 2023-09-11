#!/usr/bin/python3
"""Define an inherited class-checking function"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
