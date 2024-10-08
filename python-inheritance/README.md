# Python - Inheritance
![Python](https://github.com/user-attachments/assets/a3524d0e-dbfe-43df-bc2e-fd7b4c6e0ed9)
```markdown
# Python Inheritance

## Overview
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows one class to inherit the properties and behavior of another class. This enables code reuse and facilitates the creation of a hierarchy of related classes.

## Key Concepts
* **Base Class**: The class from which another class inherits properties and behavior. Also known as the parent class or superclass.
* **Derived Class**: The class that inherits properties and behavior from another class. Also known as the child class or subclass.
* **Inheritance**: The process by which a derived class inherits properties and behavior from a base class.

## Tasks

### 0. Lookup
Write a function that returns the list of available attributes and methods of an object:

* Prototype: `def lookup(obj):`
* Returns a list object
* You are not allowed to import any module

### 1. My list
Write a class `MyList` that inherits from `list`:

* Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
* You can assume that all the elements of the list will be of type `int`
* You are not allowed to import any module

### 2. Exact same object
Write a function that returns `True` if the object is exactly an instance of the specified class; otherwise `False`.

* Prototype: `def is_same_class(obj, a_class):`
* You are not allowed to import any module

### 3. Same class or inherit from
Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`.

* Prototype: `def is_kind_of_class(obj, a_class):`
* You are not allowed to import any module

### 4. Only sub class of
Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`.

* Prototype: `def inherits_from(obj, a_class):`
* You are not allowed to import any module

### 5. Geometry module
Write an empty class `BaseGeometry`.

* You are not allowed to import any module

### 6. Improve Geometry
Write a class `BaseGeometry` (based on `5-base_geometry.py`).

* Public instance method: `def area(self):` that raises an Exception with the message `area() is not implemented`
* You are not allowed to import any module

### 7. Integer validator
Write a class `BaseGeometry` (based on `6-base_geometry.py`).

* Public instance method: `def area(self):` that raises an Exception with the message `area() is not implemented`
* Public instance method: `def integer_validator(self, name, value):` that validates `value`:
    * you can assume `name` is always a string
    * if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
    * if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`
* You are not allowed to import any module

### 8. Rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).

* Instantiation with `width` and `height`: `def __init__(self, width, height):`
    * `width` and `height` must be private. No getter or setter
    * `width` and `height` must be positive integers, validated by `integer_validator`

### 9. Full rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)

* Instantiation with `width` and `height`: `def __init__(self, width, height):`
    * `width` and `height` must be private. No getter or setter
    * `width` and `height` must be positive integers validated by `integer_validator`
* The `area()` method must be implemented
* `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

### 10. Square #1
Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):

* Instantiation with `size`: `def __init__(self, size):`
    * `size` must be private. No getter or setter
    * `size` must be a positive integer, validated by `integer_validator`
* The `area()` method must be implemented

### 11. Square #2
Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).

* Instantiation with `size`: `def __init__(self, size):`
    * `size` must be private. No getter or setter
    * `size` must be a positive integer, validated by `integer_validator`
* The `area()` method must be implemented
* `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`

---

This is a Holberton School Project  
**Author**: Alexis Rodriguez Rodriguez  
**Location**: Montevideo, Uruguay  
**Date**: September 2024

© 2024 Alexis-Holberton School -- All rights reserved --
```