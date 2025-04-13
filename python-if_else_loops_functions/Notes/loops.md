# Loops in Python

Loops in Python allow you to repeat blocks of code automatically. There are two main types: the while loop and the for loop.

## While Loop

The while loop executes a block of code as long as the given condition evaluates to true. It's useful when you don't know how many times the loop will repeat, but the repetition depends on a condition.

Example:

```python
counter = 0
while counter < 5:
    print("Counter:", counter)
    counter += 1  # Increments the counter
```

In this example, as long as counter is less than 5, its value will be printed and incremented by 1 in each iteration.

## For Loop

The for loop is used to iterate over a sequence (such as a list, a string, a tuple, etc.) or over a range of numbers. It's the most common and "Pythonic" way to traverse elements.

Example with range():

```python
for i in range(5):
    print("Value:", i)
```

Here, range(5) generates a sequence of numbers from 0 to 4 and the loop prints them one by one.

Example iterating over a list:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)
```

In this case, the loop goes through each element of the fruits list and prints it.

## Summary

- **while**: Executes as long as a condition is true.
- **for**: Iterates over each element of a sequence or range of numbers.

These structures allow you to effectively control the flow of execution in your program and are fundamental in programming with Python.
