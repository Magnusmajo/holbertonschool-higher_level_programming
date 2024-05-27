#!/usr/bin/env python3
"""
Abstract Animals
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    This is a base class for all animals.
    """

    @abstractmethod
    def sound(self):
        """
        This method should be implemented
        by all subclasses to make a sound.
        """
        pass

class Dog(Animal):
        """
        This is a subclass of Animal.
        Args:
        Animal (_dog_): return bark
        """

    def sounf(self):
        """
        This method returns the sound of a dog.
        """
        return "Bark0!"

class Cat(Animal):
    """
    This is a subclass of Animal.
    """

    def sound(self):
        """
        This method returns the sound of a cat.
        """
        return "Meow!"
