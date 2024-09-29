#!/usr/bin/python3
""" Task 02: Abstract class
Module that defines a class Shape """


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """ An abstract class that defines a method that must be implemented in subclasses """

    @abstractmethod
    def area(self):
        """ Abstract method that defines the area of the shape """
        pass

    @abstractmethod
    def perimeter(self):
        """ Abstract method that defines the perimeter of the shape """
        pass

class Circle(Shape):
    """ Class Circle;
    Subclass of Shape that implements the area and perimeter methods """

    def __init__(self, radius):
        """ Constructor of the class Circle """
        self.radius = radius

    def area(self):
        """ Method that calculates the area of a circle """
        return pi * self.radius ** 2

    def perimeter(self):
        """ Method that calculates the perimeter of a circle """
        return 2 * pi * self.radius

class Rectangle(Shape):
    """ Class Rectangle;
    Subclass of Shape that implements the area and perimeter methods """

    def __init__(self, width, height):
        """ Constructor of the class Rectangle """
        self.width = width
        self.height = height

    def area(self):
        """ Method that calculates the area of a rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Method that calculates the perimeter of a rectangle """
        return 2 * (self.width + self.height)

    def shape_info(shape):
        """shape info"""
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")
