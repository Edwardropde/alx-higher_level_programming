#!/usr/bin/python3
"""
100-append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append line of text after each line containing specific string in file

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line
        new_string (str): string to append after lines with search string
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, mode='w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
