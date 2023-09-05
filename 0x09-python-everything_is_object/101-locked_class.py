#!/usr/bin/python3

class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes
    except if the new instance attribute is called first_name

    Attributes:
        first_name (str): first name of something
    """
    # Define the allowed attribute(s) using __slots_
    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new instances of Locked Class."""

        # Initialize the allowed attribute 'first_name'
        self.first_name = "first_name"
