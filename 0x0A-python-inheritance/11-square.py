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
            Exception: Always raises an Exception with the specified message.
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

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle

        Returns:
            str: A string description of the rectangle.
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

# Define a Square class that inherits from Rectangle.
class Square(Rectangle):
    """
    A class representing a square, which is a special case of a rectangle

    Attributes:
        __size (int): The size of the square.
    """

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
        """
        Returns a string representation of the square

        Returns:
            str: A string description of the square.
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
