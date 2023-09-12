#!/usr/bin/python3
"""Defines a function to write string to text file and return # of char"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8), return number of characters written.

    Args:
        filename (str): The name of the text file to write to
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "The School is so cool!\n")
    print(nb_characters)
