#!/usr/bin/python3i
# Define a function that returns True if the object is an instance of,
# or if the object is an instance of a class
# that inherited fr, the specified class; otherwise, False.

def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or inherited fr class

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass
    """
    return isinstance(obj, a_class)
