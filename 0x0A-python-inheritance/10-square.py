#!/usr/bin/python3
"""Define rectangle subclass of square."""
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

    def __str__(self):
        """Returns a string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
