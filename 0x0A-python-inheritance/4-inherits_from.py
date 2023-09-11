#!/usr/bin/python3i
# Define a function that returns True if the object is an instance of a class
# that inherited (directly or indirectly)
# from the specified class; otherwise, False
def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class
    """
    return (issubclass(type(obj), a_class))
