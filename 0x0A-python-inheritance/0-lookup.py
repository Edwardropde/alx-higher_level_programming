#!/usr/bin/python3i
# Define a function that returns the list of available attributes and methods

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        A list of attribute and method names.
    """
    return dir(obj)
