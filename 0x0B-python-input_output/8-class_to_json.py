#!/usr/bin/python3
""" Module to convert a class object to a JSON-serializable dictionary"""


def class_to_json(obj):
    """
    Convert a class object to a JSON-serializable dictionary

    Args:
        obj: The class object to convert.

    Returns:
        dict: A dictionary representing the class object.
    """
    return obj.__dict__
