# How to use the if, if ... else statements

In Python, conditional statements allow you to execute different blocks of code depending on whether a condition is met or not. The basic syntax is as follows:

1. If statement  
The `if` keyword is followed by a condition (which must evaluate to `True` or `False`) and a colon. Then, you write the block of code to execute if the condition is true, using consistent indentation.

```python
number = 10

if number > 5:
    print("The number is greater than 5")
```

In this example, if the variable `number` is greater than 5, the message is printed.

1. If ... else statement  
If you want to execute one block of code when the condition is true and a different block when it is false, you can use `else`:

```python
number = 3

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
```

Here, if the number is divisible by 2, the `if` block is executed; otherwise, the `else` block is executed.

1. Using elif for multiple conditions  
When you have more than two cases to evaluate, you can use `elif` (else if) to check additional conditions:

```python
number = 0

if number > 0:
    print("The number is positive")
elif number == 0:
    print("The number is zero")
else:
    print("The number is negative")
```

In this example, the conditions are evaluated in order until one is true. If none of the previous conditions are true, the `else` block is executed.

## Important Notes  

- **Indentation**: Indentation is crucial in Python as it defines the blocks of code that belong to each conditional statement.  
- **Boolean Evaluation**: Any value in Python can be evaluated in a boolean context; for example, zero numbers, empty strings, empty lists, and `None` are considered `False`.  

These conditional structures make the code clear and readable, allowing you to handle different execution flows based on defined conditions.
