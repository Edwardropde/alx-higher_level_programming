#!/usr/bin/python3
# Define a BaseGeometry class.

class BaseGeometry:
    """
    A base class for geometry-related operations.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented"

        Raises:
            Exception: Always raises an Exception with the specified message
        """
        raise Exception("area() is not implemented")
