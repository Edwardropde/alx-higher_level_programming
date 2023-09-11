#!/usr/bin/python3
# Define a class MyList that inherits fr list

class MyList(list):
    """
    A custom list class that inherits fr the built-in list class

    Public instance method:
        Prints the list in ascending order
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
