#!/usr/bin/python3

class Rectangle:
    """
    A class that defines a rectangle.

    Attributes:
        __width (int)
        __height (int)
    """

    number_of_instances = 0  # Class attribute to track the number of instances

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with height and width

        Args:
            width (int)
            height (int)
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1  # Increment the instance count

    @property
    def width(self):
        """
        Getter method for retrieving rectangle width

        Returns:
            Rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting rectangle width

        Args:
            value rep width value to set

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
        Getter method for retrieving rectangle height

        Returns:
            Rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting rectangle height

        Args:
            value representing height to set

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Public method that calculates and returns rectangle area

        Returns:
            Rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public method that calculates and returns rectangle perimeter

        Returns:
            Rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += ('#' * self.__width + '\n')
        return rectangle_str[:-1]

    def __repr__(self):
        """
        Returns string representation of rectangle object to recreate with eval
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted
        decrements the instance count
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
