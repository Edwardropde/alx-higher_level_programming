#!/usr/bin/python3
"""
Module 3-square

Defines a class Square with private instance attribute, validation, and area
"""

class Square:
    """
    Defines a square with a private instance attribute.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size ** 2)
