#!/usr/bin/python3
"""Module for SinglyLinkedList class."""


class Node:
    """A class named Node, that defines a node of a singly linked list."""
    def __init__(self, data, next_node=None):
        """Initializes the Node instance.
        Args:
            data (int): The data of the node.
            next_node (Node): The next node of the New Node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node.
        Args:
            value (int): The data of the node.
            Raises:
                TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node.
        Args:
            value (Node): The next node.
            Raises:
                TypeError: If next_node is not a Node object.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """A class named SinglyLinkedList that defines a singly linked list."""
    def __init__(self):
        """Initializes the SinglyLinkedList instance."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list.
        Args:
            value (int): The value of the new Node.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the SinglyLinkedList instance."""
        current = self.__head
        result = ""
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
