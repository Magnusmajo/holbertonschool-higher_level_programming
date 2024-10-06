#!/usr/bin/python3
"""
Pickling Custom Classes
"""
import pickle 


class CustomObject:
    """A custom object with name, age,
    and is_student attributes."""

    def __init__(self, name, age, is_student):
        """Initializing the object with the given name, age,
        and is_student values."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displaying the name, age, and is_student attributes
        of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializing the object and saving it to a file."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            """Printing an error message if serialization fails."""
            print(f"An error occurred while serializing: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializing the object from a file."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            """Printing an error message if deserialization fails."""
            print(f"An error occurred while deserializing: {e}")
            return None
