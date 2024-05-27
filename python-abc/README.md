# Python - Abstract Classes and Interfaces


1. Shapes, Interfaces, and Duck Typing
mandatory
Background:
Python employs a concept called “duck typing,” which is concerned with the semantics
of objects rather than their inheritance hierarchy. If an object behaves like a duck
(i.e., has all the methods and properties of a duck), then it’s considered a duck,
regardless of its actual class. This concept allows for flexible and dynamic polymorphism.

In this exercise, we’ll use abstract base classes to design a blueprint for shapes and use duck
typing to handle objects of different shapes uniformly.

Objective:
Create an abstract class named Shape with two abstract methods: area and perimeter.
Implement two concrete classes: Circle and Rectangle, both inheriting from Shape. Each class
should provide implementations for the area and perimeter methods.
Write a standalone function named shape_info that accepts an object of type Shape (by duck typing) and prints its area and perimeter.
Test the shape_info function with instances of both Circle and Rectangle.
Instructions:
Shape Abstract Class:

Define an abstract class Shape using the ABC package.
Within Shape, declare two abstract methods: area and perimeter.
Circle and Rectangle Classes:

Create a Circle class that inherits from Shape. The constructor (__init__) should accept a radius. Implement the area and perimeter methods.
Create a Rectangle class, also inheriting from Shape. Its constructor should accept the width and height. Implement the area and perimeter methods.
shape_info Function:

Define a function named shape_info that takes a single argument.
Without explicitly checking the type of the argument, call its area and perimeter methods (relying on duck typing).
Print the area and perimeter of the shape passed to the function.
Testing:

Instantiate a Circle and a Rectangle.
Pass each object to the shape_info function and observe the output.
Hints:

While Python doesn’t enforce interfaces in the same way as statically-typed languages, abstract base classes provide a mechanism to ensure
certain methods are implemented in subclasses.
Duck typing in the shape_info function implies that you shouldn’t use isinstance checks. Instead,
trust that the passed object adheres to the Shape interface.

###  2. Extending the Python List with Notifications
mandatory
Background:
In Python, you can extend built-in classes to add or modify behavior. The list class provides a collection of methods and functionalities that handle list operations. By extending the list class, you can provide custom behaviors while retaining the original functionalities.

Objective:
Create a class named VerboseList that extends the Python list class. This custom class should print a notification message every time an item is added (using the append or extend methods) or removed (using the remove or pop methods).

Instructions:
Setting up the VerboseList Class:

Define a class VerboseList that inherits from the built-in list class.
Within VerboseList, override the methods that modify the list: append, extend, remove, and pop.
Implementing Notifications:

For the append method: After adding the item to the list, print a message like “Added [item] to the list.”
For the extend method: After extending the list, print a message like “Extended the list with [x] items.” where [x] is the number of items added.
For the remove method: Before removing the item from the list, print a message like “Removed [item] from the list.”
For the pop method: Before popping the item from the list, print a message like “Popped [item] from the list.” If the index is not specified, default behavior is to pop the last item.
Testing:

Instantiate a VerboseList object.
Test all the overridden methods (append, extend, remove, and pop) and ensure that the appropriate messages are printed for each operation.
Hints:

Remember to call the original method of the list class using the super() function to ensure that the original functionality is retained. For example, for append: super().append(item).
Think about edge cases, such as trying to remove an item that doesn’t exist in the list.