#!/usr/bin/python3
"""
Module 100-singly_linked_list

Defines classes Node and SinglyLinkedList for a singly linked list.
"""

class Node:
    """
    A class representing a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node (private).
        __next_node (Node): The next node in the linked list
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node instance

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The next node in the linked list. Defaults to None
        """
        self.data = data
        self.next_node = next_node

        if not isinstance(data, int):
            raise TypeError("data must be an integer")

    @property
    def data(self):
        """
        Get the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node.

        Args:
            value (int): The new data to be stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        Args:
            value (Node): The new next node in the linked list.

        Raises:
            TypeError: If value is not a Node object.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head: The head node of the linked list.
    """
    def __init__(self):
        """
        Initializes a SinglyLinkedList instance.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the linked list

        Args:
            value (int): The value of the new Node to be inserted.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Generates a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return (result.rstrip("\n"))
