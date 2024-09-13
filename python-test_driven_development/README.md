# Python - Test-driven development

=====================================
Test-Driven Development (TDD) in Python
Test-Driven Development (TDD) is a software development methodology where tests are written before the production code. The process follows these steps:

Write a Test: Before writing any functional code, write a test that defines a small improvement or new functionality.
Run the Test: Run the test to ensure it fails, as the functionality hasn’t been implemented yet.
Write the Code: Write the minimal code necessary to make the test pass.
Refactor: Improve the code while ensuring all tests still pass.
Repeat: Repeat the cycle for each new functionality or improvement.
Benefits of TDD
Improves Code Quality: Writing tests first ensures the code meets requirements from the start.
Easier Maintenance: Tests act as living documentation of the code, making it easier to detect bugs and understand the system’s functionality.
Encourages Modular Design: TDD promotes writing code in small, functional units, which makes it easier to reuse and maintain.
Common Tools in Python
pytest: A powerful tool for writing and running tests.
unittest: Python’s standard module for unit testing.
pydantic: Useful for data validation and reducing the number of necessary tests
=====================================

### 0. Integers addition

Write a function that adds 2 integers.

Prototype: def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
You are not allowed to import any module.

###  1.Divide a matrix

Write a function that divides all elements of a matrix.

Prototype: def matrix_divided(matrix, div):
matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
All elements of the matrix should be divided by div, rounded to 2 decimal places
Returns a new matrix
You are not allowed to import any module

### 2. Say my name

Write a function that prints My name is <first name> <last name>

Prototype: def say_my_name(first_name, last_name=""):
first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string
You are not allowed to import any module

### 3. Print square

Write a function that prints a square with the character #.

Prototype: def print_square(size):
size is the size length of the square
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
if size is a float and is less than 0, raise a TypeError exception with the message size must be an integer
You are not allowed to import any module

### 4. Text indentation

Write a function that prints a text with 2 new lines after each of these characters: ., ? and :

Prototype: def text_indentation(text):
text must be a string, otherwise raise a TypeError exception with the message text must be a string
There should be no space at the beginning or at the end of each printed line
You are not allowed to import any module

### 5. Max integer - Unittest

Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function def max_integer(list=[]):.

Your test file should be inside a folder tests
You have to use the unittest module
Your test file should be python files (extension: .py)
Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
All tests you make must be passable by the function below
We strongly encourage you to work together on test cases, so that you don’t miss any edge case

This is an Holberton School Project Author: Alexis Rodriguez Rodriguez Location: Montevideo. Uruguay September 2024

@ 2024 Alexis-Holberton School --All right reserved--
