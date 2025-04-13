# How to affect values to variables

In Python, assigning a value to a variable is very simple and is done using the assignment operator =. This means that when you write:

```python
x = 5
```

you're "assigning" the value 5 to the variable x. It's not necessary to declare the variable type beforehand; Python is a dynamically typed language, so the type is automatically determined based on the assigned value.

Some additional examples are:

Simple assignment:

```python
message = "Hello, world"
```

Multiple assignment in a single line:
You can assign the same value to multiple variables at once:

```python
a = b = c = 0
```

Or assign different values through unpacking:

```python
x, y, z = 1, 2, 3
```

Reassignment:
If you assign a new value to a variable, the previous value is replaced:

```python
counter = 10
counter = counter + 1  # Now counter is 11
```

This form of assignment is fundamental in Python and is used throughout code to store and manipulate data.
