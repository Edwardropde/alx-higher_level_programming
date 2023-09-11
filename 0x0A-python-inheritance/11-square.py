#!/usr/bin/python3
"""Define a Square class that inherits Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A class representing a square"""

    def __init__(self, size):
        """
        Initializes a Square instance with size.

        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", self.__size)
