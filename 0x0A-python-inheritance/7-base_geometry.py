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

    def integer_validator(self, name, value):
        """
        Validates the value and raises exceptions if it doesn't meet criteria"

        Args:
            name (str): The name of the value being validated.
            value: The value to validate.

        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
