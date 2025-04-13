# How to Use `range()` in Python

The `range()` function generates a sequence of numbers and is commonly used for looping a specific number of times in `for` loops. Here's how to use it effectively:

## Basic Syntax

```python
range(stop)              # 0 to stop-1
range(start, stop)       # start to stop-1
range(start, stop, step) # start to stop-1 with step size
```

## Common Use Cases

1. **Simple range (0 to n-1)**

    ```python
    for i in range(5):
         print(i)  # Output: 0 1 2 3 4
    ```

2. **Specifying start and end**

    ```python
    for i in range(2, 6):
         print(i)  # Output: 2 3 4 5
    ```

3. **Using a step value**

    ```python
    for i in range(0, 10, 2):
         print(i)  # Output: 0 2 4 6 8
    ```

4. **Counting backwards**

    ```python
    for i in range(5, 0, -1):
         print(i)  # Output: 5 4 3 2 1
    ```

## Important Characteristics

- **Memory efficient**: `range()` doesn't create an actual list; it generates numbers on demand.
- **Exclusive stop**: The sequence never includes the stop value.
- **Immutable sequence**: You can't modify a `range` object after creation.

## Converting to Lists

```python
numbers = list(range(5))         # [0, 1, 2, 3, 4]
evens = list(range(0, 10, 2))    # [0, 2, 4, 6, 8]
```

## Practical Examples

1. **Iterating through list indices**

    ```python
    fruits = ['apple', 'banana', 'cherry']
    for i in range(len(fruits)):
         print(f"Index {i}: {fruits[i]}")
    ```

2. **Creating mathematical sequences**

    ```python
    squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    ```

3. **Implementing repeat actions**

    ```python
    for _ in range(3):  # Convention: _ when variable isn't used
         print("Hello!")  # Prints "Hello!" three times
    ```

## Python 2 vs Python 3 Note

In Python 2, `range()` created an actual list, while Python 3's `range()` is more memory efficient. Python 2 had `xrange()` which behaved like Python 3's `range()`.
