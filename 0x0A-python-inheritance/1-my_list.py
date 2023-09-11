#!/usr/bin/python3
"""Define a class MyList that inherits list"""

class MyList(list):
    """Implements sorted printing for built in list"""

    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
