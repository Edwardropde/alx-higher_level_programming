#!/usr/bin/python3
# Define a MyInt class that inherits fr int.

class MyInt(int):
    """
    A class representing MyInt, which is a rebel integer
    """

    def __eq__(self, other):
        """
        Inverts the equality operator (==).

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are not equal
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the inequality operator (!=).

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are equal, False otherwise
        """
        return super().__eq__(other)
