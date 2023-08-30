#!/usr/bin/python3
"""
Module 103-magic_class

Defines class MagicClass to match the given Python bytecode.
"""

import math

class MagicClass:
    """
    A class representing a MagicClass.

    Attributes:
        __radius (float): The radius of the magic circle (private).
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance.

        Args:
            radius (float, optional): The radius of the magic circle. Defaults to 0.
            """
        self.__radius = 0
        self.__radius = radius

    @property
    def radius(self):
        """
        Get the radius of the magic circle.

        Returns:
            float: The radius of the magic circle.
        """
        return (self.__radius)

    @radius.setter
    def radius(self, value):
        """
        Set the radius of the magic circle.

        Args:
            value (float): The new radius of the magic circle.

        Raises:
            TypeError: If value is not a number (float or integer).
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        """
        Calculate and return the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Calculate and return the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return (2 * math.pi * self.__radius)
