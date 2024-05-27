#!/usr/bin/python3
"""
Abstract Animals
"""


from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract class for animals
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to make a sound
        """
        pass

class Dog(Animal):
    """
    Concrete class for dogs
    """

    def sound(self):
        """
        Concrete method to make a sound for dogs
        """

        return "Bark"

class Cat(Animal):
    """
    Concrete class for cats
    """

    def sound(self):
        """
        Concrete method to make a sound for cats
        """

        return "Meow"
