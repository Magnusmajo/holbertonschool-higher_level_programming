# How to use comments

Comments in Python are used to explain and document the code so that both you and other developers can better understand what the program does. Here are the main ways to use them:

1. Single-line comments  
To comment a single line (or part of it), use the hash symbol (`#`). Everything to the right of the `#` is ignored by the interpreter.

```python
# This is a comment explaining what the next line does
print("Hello, world")  # This comment is at the end of the line
```

1. Multi-line comments  
Python does not have a specific syntax for block comments (like `/* ... */` in other languages). The usual way to write comments spanning multiple lines is to place `#` at the beginning of each line:

```python
# This block of comments
# explains in detail what
# a complex code fragment does.
```

Although multi-line strings (enclosed in triple quotes) are sometimes used to simulate comments, they are interpreted as docstrings if placed in strategic locations (such as at the beginning of modules, classes, or functions) and serve a documentation purpose.

1. Docstrings  
A docstring is a documentation string placed at the beginning of a module, class, or function to explain its purpose. Although technically they are strings, they are used as documentation comments and can be accessed through the `help()` function or the `__doc__` attribute.

```python
def add(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b
```

**Summary**  

- **Single-line comments**: Use `#` for single-line comments or to annotate parts of the code.  
- **Block comments**: Write `#` at the beginning of each line.  
- **Docstrings**: Use triple quotes to document modules, classes, and functions.  

These practices not only help to better understand the code but also make it easier to maintain and collaborate with other developers.
