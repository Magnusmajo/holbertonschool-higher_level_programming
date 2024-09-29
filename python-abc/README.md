# Python - Abstract Classes and Interfaces
```markdown
# Abstract Classes and Interfaces in Python

## Overview

Abstract classes and interfaces are used to define a blueprint for other classes to follow. They cannot be instantiated on their own and are meant to be inherited by other classes.

## 0. Abstract Animal Class and its Subclasses


### Background

In object-oriented programming, Abstract Base Classes (ABCs) ensure that derived classes implement specific methods from the base class. This provides a blueprint for creating and structuring derived classes. Python’s ABC package facilitates the creation of abstract base classes.

### Objective

- Create an abstract class named `Animal` using the ABC package. This class should have an abstract method called `sound`.
- Create two subclasses of `Animal`: `Dog` and `Cat`. Implement the `sound` method in each subclass to return the strings “Bark” and “Meow” respectively.

### Resources

- [Python ABC documentation](https://docs.python.org/3/library/abc.html)

### Instructions

#### Setting up the Abstract Class

1. Import the necessary components from the `abc` module.
2. Define the `Animal` class, ensuring it inherits from `ABC` to mark it as abstract.
3. Inside the `Animal` class, declare an abstract method named `sound` using the `@abstractmethod` decorator.

#### Implementing the Subclasses

1. Create a subclass named `Dog` that inherits from the `Animal` class.
2. Implement the `sound` method in the `Dog` class to return the string “Bark”.
3. Similarly, create a subclass named `Cat` that also inherits from the `Animal` class.
4. Implement the `sound` method in the `Cat` class to return the string “Meow”.

## 1. Shapes, Interfaces, and Duck Typing


### Background

Python employs a concept called “duck typing,” which is concerned with the semantics of objects rather than their inheritance hierarchy. If an object behaves like a duck (i.e., has all the methods and properties of a duck), then it’s considered a duck, regardless of its actual class. This concept allows for flexible and dynamic polymorphism.

In this exercise, we’ll use abstract base classes to design a blueprint for shapes and use duck typing to handle objects of different shapes uniformly.

### Objective

- Create an abstract class named `Shape` with two abstract methods: `area` and `perimeter`.
- Implement two concrete classes: `Circle` and `Rectangle`, both inheriting from `Shape`. Each class should provide implementations for the `area` and `perimeter` methods.
- Write a standalone function named `shape_info` that accepts an object of type `Shape` (by duck typing) and prints its area and perimeter.
- Test the `shape_info` function with instances of both `Circle` and `Rectangle`.

### Resources

- [Python ABC documentation](https://docs.python.org/3/library/abc.html)
- [Concept of Duck Typing](https://realpython.com/lessons/duck-typing/)

### Instructions

#### Shape Abstract Class

1. Define an abstract class `Shape` using the ABC package.
2. Within `Shape`, declare two abstract methods: `area` and `perimeter`.

#### Circle and Rectangle Classes

1. Create a `Circle` class that inherits from `Shape`. The constructor (`__init__`) should accept a radius. Implement the `area` and `perimeter` methods.
2. Create a `Rectangle` class, also inheriting from `Shape`. Its constructor should accept the width and height. Implement the `area` and `perimeter` methods.

#### shape_info Function

1. Define a function named `shape_info` that takes a single argument.
2. Without explicitly checking the type of the argument, call its `area` and `perimeter` methods (relying on duck typing).
3. Print the area and perimeter of the shape passed to the function.

#### Testing

1. Instantiate a `Circle` and a `Rectangle`.
For the pop method: Before popping the item from the list, print a message like “Popped [item] from the list.” If the index is not specified, default behavior is to pop the last item.
2. Pass each object to the `shape_info` function and observe the output.

## 2. Extending the Python List with NotificationsInstantiate a VerboseList object.
append, extend, remove, and pop) and ensure that the appropriate messages are printed for each operation.

### 3. CountedIterator - Keeping Track of Iteration
### Background
d:
In Python, you can extend built-in classes to add or modify behavior. The `list` class provides a collection of methods and functionalities that handle list operations. By extending the `list` class, you can provide custom behaviors while retaining the original functionalities. allows a new class to inherit properties and methods from an existing class. In Python, many built-in classes can be extended to customize or enhance their behavior. The iter function, which returns an iterator object, provides the __next__ method to fetch the next item in the sequence. This exercise focuses on extending the functionality of this iterator object.

### ObjectiveObjective:
lass named CountedIterator that extends the built-in iterator obtained from the iter function. The CountedIterator should keep track of the number of items that have been iterated over. Specifically, you will need to override the __next__ method to increment a counter each time an item is fetched.
Create a class named `VerboseList` that extends the Python `list` class. This custom class should print a notification message every time an item is added (using the `append` or `extend` methods) or removed (using the `remove` or `pop` methods).
Instructions:
### Instructionse CountedIterator Class:

#### Setting up the VerboseList ClassDefine a class CountedIterator.
initialize two attributes: the iterator object (using the iter function) and a counter to track the number of items iterated.
1. Define a class `VerboseList` that inherits from the built-in `list` class.
2. Within `VerboseList`, override the methods that modify the list: `append`, `extend`, `remove`, and `pop`.

#### Implementing NotificationsWithin the CountedIterator class, override the __next__ method.
thod is called.
1. For the `append` method: After adding the item to the list, print a message like “Added [item] to the list.”items left to iterate, the method should raise the StopIteration exception.
2. For the `extend` method: After extending the list, print a message like “Extended the list with [x] items.” where [x] is the number of items added.
3. For the `remove` method: Before removing the item from the list, print a message like “Removed [item] from the list.”
4. For the `pop` method: Before popping the item from the list, print a message like “Popped [item] from the list.” If the index is not specified, default behavior is to pop the last item.Instantiate a CountedIterator object using a list or another iterable.
.
#### Testing have been fetched

1. Instantiate a `VerboseList` object.### 4. The Enigmatic FlyingFish - Exploring Multiple Inheritance
2. Test all the overridden methods (`append`, `extend`, `remove`, and `pop`) and ensure that the appropriate messages are printed for each operation.
d:
## 3. CountedIterator - Keeping Track of Iterationect-oriented languages, a class can inherit attributes and behaviors from more than one parent class. This is known as multiple inheritance. Python is one of the languages that supports multiple inheritance, which can be a powerful tool, but it also comes with complexities, particularly regarding method resolution order (MRO).

Objective:
a FlyingFish class that inherits from both a Fish class and a Bird class. Within FlyingFish, override methods from both parents. The goal is to comprehend multiple inheritance and how Python determines method resolution order.
### Background
Instructions:
Subclassing allows a new class to inherit properties and methods from an existing class. In Python, many built-in classes can be extended to customize or enhance their behavior. The `iter` function, which returns an iterator object, provides the `__next__` method to fetch the next item in the sequence. This exercise focuses on extending the functionality of this iterator object.s Setup:

### ObjectiveCreate a Fish class with methods swim (which prints “The fish is swimming”) and habitat (which prints “The fish lives in water”).

Create a class named `CountedIterator` that extends the built-in iterator obtained from the `iter` function. The `CountedIterator` should keep track of the number of items that have been iterated over. Specifically, you will need to override the `__next__` method to increment a counter each time an item is fetched.

### InstructionsConstruct a FlyingFish class that inherits from both Fish and Bird.

#### Setting up the CountedIterator Class”.
in water and the sky!”.
1. Define a class `CountedIterator`.
2. In the constructor (`__init__`), initialize two attributes: the iterator object (using the `iter` function) and a counter to track the number of items iterated.
3. Provide a method `get_count` to return the current value of the counter.Instantiate an object of the FlyingFish class.
serve the outputs.
#### Overriding the next Method class to investigate the method resolution order. For instance, print(FlyingFish.mro()).

1. Within the `CountedIterator` class, override the `__next__` method.### 5. The Mystical Dragon - Mastering Mixins
2. In this method, increment the counter each time the `__next__` method is called.
3. Fetch the next item from the original iterator and return it. If there are no items left to iterate, the method should raise the `StopIteration` exception.d:
a way to add functionality to classes in a modular fashion. They’re not meant to stand alone but are meant to be combined with other classes to add behaviors. By using mixins, you can compose behaviors in classes without the need for deep or rigid inheritance hierarchies.
#### Testing
Objective:
1. Instantiate a `CountedIterator` object using a list or another iterable. mixin classes, SwimMixin and FlyMixin, each equipped with methods swim and fly respectively. Next, construct a class Dragon that inherits from both these mixins. Your aim is to show that a Dragon instance can both swim and fly.
2. Iterate over items using a loop or manual calls to the `__next__` method.
Instructions:
3. Use the `get_count` method to retrieve and print the number of items that have been fetched.Creating Mixins:

## 4. The Enigmatic FlyingFish - Exploring Multiple Inheritancealled SwimMixin with a method swim that prints “The creature swims!”.
Design another mixin called FlyMixin with a method fly that prints “The creature flies!”.


### Backgroundmed Dragon that inherits from both SwimMixin and FlyMixin.
Within the Dragon class, you can add additional methods or attributes if desired, such as roar, which could print “The dragon roars!”.
In some object-oriented languages, a class can inherit attributes and behaviors from more than one parent class. This is known as multiple inheritance. Python is one of the languages that supports multiple inheritance, which can be a powerful tool, but it also comes with complexities, particularly regarding method resolution order (MRO).

### Objectiveagon class named draco.
Demonstrate draco‘s abilities by calling the swim, fly, and (if implemented) roar methods.
Construct a `FlyingFish` class that inherits from both a `Fish` class and a `Bird` class. Within `FlyingFish`, override methods from both parents. The goal is to comprehend multiple inheritance and how Python determines method resolution order.

### Instructions
s is a Holberton School Project  
#### Parent Classes Setup**Author**: Alexis Rodriguez Rodriguez  

1. Create a `Fish` class with methods `swim` (which prints “The fish is swimming”) and `habitat` (which prints “The fish lives in water”).
2. Create a `Bird` class with methods `fly` (which prints “The bird is flying”) and `habitat` (which prints “The bird lives in the sky”).
School -- All rights reserved --#### Implementing FlyingFish
1. Construct a `FlyingFish` class that inherits from both `Fish` and `Bird`.
2. Override the `fly` method to print “The flying fish is soaring!”.
3. Override the `swim` method to print “The flying fish is swimming!”.
4. Override the `habitat` method to print “The flying fish lives both in water and the sky!”.

#### Testing and MRO Exploration

1. Instantiate an object of the `FlyingFish` class.
2. Call the `fly`, `swim`, and `habitat` methods and observe the outputs.
3. Use the `mro()` method or the `.__mro__` attribute on the `FlyingFish` class to investigate the method resolution order. For instance, `print(FlyingFish.mro())`.

## 5. The Mystical Dragon - Mastering Mixins



### Background

Mixins are a way to add functionality to classes in a modular fashion. They’re not meant to stand alone but are meant to be combined with other classes to add behaviors. By using mixins, you can compose behaviors in classes without the need for deep or rigid inheritance hierarchies.

### Objective

Design two mixin classes, `SwimMixin` and `FlyMixin`, each equipped with methods `swim` and `fly` respectively. Next, construct a class `Dragon` that inherits from both these mixins. Your aim is to show that a `Dragon` instance can both swim and fly.

### Instructions

#### Creating Mixins

1. Design a mixin called `SwimMixin` with a method `swim` that prints “The creature swims!”.
2. Design another mixin called `FlyMixin` with a method `fly` that prints “The creature flies!”.

#### Implementing Dragon

1. Construct a class named `Dragon` that inherits from both `SwimMixin` and `FlyMixin`.
2. Within the `Dragon` class, you can add additional methods or attributes if desired, such as `roar`, which could print “The dragon roars!”.

#### Testing the Dragon’s Abilities

1. Instantiate an object of the `Dragon` class named `draco`.
2. Demonstrate `draco`‘s abilities by calling the `swim`, `fly`, and (if implemented) `roar` methods.

---

This is a Holberton School Project  
**Author**: Alexis Rodriguez Rodriguez  
**Location**: Montevideo, Uruguay  
**Date**: September 2024

© 2024 Alexis-Holberton School -- All rights reserved --
```