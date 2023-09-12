#!/usr/bin/python3
"""Defines a function to append a string to a text file and return chars"""


def append_write(filename="", text=""):
    """
     Append a string to the end of a text file (UTF8) and return # chars

     Args:
        filename (str): The name of the text file to append to
        text (str): The string to append to the file

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt", "School is cool!\n")
    print(nb_characters_added)
