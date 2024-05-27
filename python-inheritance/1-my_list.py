#!/usr/bin/python3
"""
MyList:
    A class called MyList
"""


class MyList(list):
    """
    A class that inherits from list
    Arguments:
    list: The parent class
    """
    def print_sorted(self):
        """
        Prints a sorted list
        """
        print(sorted(self))
