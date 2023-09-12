#!/usr/bin/python3
"""Student module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student

        Attributes:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the dictionary representation of a Student instance

        Args:
            attrs (list, optional): A list of attribute names. Defaults to None

        Returns:
            dict: A dictionary containing the specified attributes and values
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key,
                    value in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance

        Args:
            json (dict): A dictionary containing attribute to replace
        """
        for key, value in json.items():
            setattr(self, key, value)
