#!/usr/bin/python3

class Rectangle:
    """
    A class that defines a rectangle.

    Attributes:
        __width
        __height
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with width or length

        Args:
            width (int): default is 0
            height (int): default is 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.

        Returns:
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting rectangle width

        Args:
            value (int): width value to set

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for getting rectangle height

        Returns:
            Rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting rectangle height

        Args:
            value: Height value to set

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
