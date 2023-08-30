#!/usr/bin/python3
"""
Module 101-square

Defines class Square for a square with size and position.
"""

class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square's sides (private).
        __position (tuple): The position of the square (private).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The size of the square's sides. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).
            """
            self.size = size
            self.position = position

        @property
        def size(self):
            """
            Get the size of the square's sides.

            Returns:
                int: The size of the square's sides.
            """
            return (self.__size)

        @size.setter
        def size(self, value):
            """
            Set the size of the square's sides.

            Args:
                value (int): The new size of the square's sides.

            Raises
                TypeError: If value is not an integer.
                ValueError: If value is less than 0.
            """
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        @property
        def position(self):
            """
            Get the position of the square.

            Returns:
                tuple: The position of the square
            """
            return (self.__position)

        @position.setter
        def position(self, value):
            """
            Set the position of the square.

            Args:
                value (tuple): The new position of the square.

            Raises:
                TypeError: If value is not a tuple of 2 positive integers.
            """
            if not isinstance(value, tuple) or len(value) != 2:
                raise TypeError("position must be a tuple of 2 positive integers")
            if not all(isinstance(x, int) and x >= 0 for x in value):
                raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

        def area(self):
            """
            Calculate and return the area of the square.

            Returns:
                int: The area of the square.
            """
            return (self.__size ** 2)

        def my_print(self):
            """
            Print the square using '#' characters
            """
            if self.__size == 0:
                print()
                return
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
