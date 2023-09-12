#!/usr/bin/python3
"""Defines a function to read and print the content of a text file."""


def read_file(filename=""):
    """
    Read a text file (UTF8) and print its content to stdout

    Args:
        filename (str): The name of the text file to read.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')


if __name__ == "__main__":
    read_file()
