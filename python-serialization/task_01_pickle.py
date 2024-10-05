#!/usr/bin/python3
"""Pickling custon class"""
import pickle


class CustonObject:
    """A custom Python class"""

    def __init__(self, name, age, is_student):
        """
        Initialize the object with the provided name, age and student status.
        Args:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): The student status of the person.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name},
            Age: {self.age},
            Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializing the object and saving it into a file"""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
