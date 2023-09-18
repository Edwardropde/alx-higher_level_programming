#!/usr/bin/python3
"""Base for all other bases"""


import json


class Base:
    """
    Base model. Represents the "base" for all other classes.

    Attributes:
        __nb_objects (int): Number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation

        Args:
            list_dictionaries (list of dict): list of dictionaries to convert

        Returns:
            str: JSON string representation of the list of dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file

        Args:
            list_objs (list of Base instances)

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []

        json_data = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(json_data)

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string representation to a list of dictionaries

        Args:
            json_string (str): JSON string to convert.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set from a dictionary

        Args:
            cls: Class reference.
            **dictionary: Dictionary with attribute values

        Returns:
            Base: Instance with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file and return a list of instances

        Returns:
             list: List of instances loaded from the JSON file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_str = file.read()
                json_list = json.loads(json_str)
                instances = [cls.create(**data) for data in json_list]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the CSV representation of list_objs to a file

        Args:
            list_objs (list of Base instances): List of objects to serialize

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []

            filename = cls.__name__ + ".csv"
            with open(filename, "w", newline="") as file:
                csv_writer = csv.writer(file)
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        data = [obj.id, obj.width, obj.height, obj.x, obj.y]
                    elif cls.__name__ == "Square":
                        data = [obj.id, obj.size, obj.x, obj.y]
                    csv_writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """
        Load objects from a CSV file and return a list of instances

        Returns:
            list of Base instances: List of objects loaded from the file
        """
        filename = cls.__name__ + ".csv"
        instance_list = []
        try:
            with open(filename, "r") as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    row = [int(x) for x in row]
                    if cls.__name__ == "Rectangle":
                        instance = cls(row[1], row[2], row[3], row[4], row[0])
                    elif cls.__name__ == "Square":
                        instance = cls(row[1], row[2], row[3], row[0])
                    instance_list.append(instance)
        except FileNotFoundError:
            pass
        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Open window and draw all Rectangles and Squares using Turtle Graphix

        Args:
            list_rectangles (list of Rectangle)
            list_squares (list of Square)

        Return:
            None
        """
        screen = turtle.Screen()
        screen.title("Turtle Drawing")

        # Create a turtle object for drawing
        t = turtle.Turtle()
        t.speed(1)  # Set the drawing speed

        # Draw Rectangles
        for rectangle in list_rectangles:
            t.penup()
            t.goto(rectangle.x, rectangle.y)
            t.pendown()
            for i in range(2):
                t.forward(rectangle.width)
                t.left(90)
                t.forward(rectangle.height)
                t.left(90)
            t.penup()

        # Draw Squares
        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for i in range(4):
                t.forward(square.size)
                t.left(90)
            t.penup()

        # Close the window on click
        screen.exitonclick()
