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
        Validates the value and raises exceptions if criteria not met
        
        Args:
            name (str): The name of the value being validated.
            value: The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

# Define a Rectangle class that inherits from BaseGeometry.

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
