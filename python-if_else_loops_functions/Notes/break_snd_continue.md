# Using break and continue Statements in Loops

The `break` and `continue` statements are control flow tools that help you manage loops more effectively.

## `break` Statement

The `break` statement terminates the loop immediately and continues execution after the loop.

```python
# Example: break in a while loop
count = 0
while count < 5:
    if count == 3:
        break  # Exit the loop when count is 3
    print(count)
    count += 1
# Output: 0 1 2
```

```python
# Example: break in a for loop
for num in range(10):
    if num == 5:
        break  # Exit when num reaches 5
    print(num)
# Output: 0 1 2 3 4
```

## `continue` Statement

The `continue` statement skips the rest of the current iteration and moves to the next iteration.

```python
# Example: continue in a for loop
for num in range(5):
    if num == 2:
        continue  # Skip printing 2
    print(num)
# Output: 0 1 3 4
```

```python
# Example: continue in a while loop
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip printing 3
    print(count)
# Output: 1 2 4 5
```

## Key Differences

- **`break`**: Exits the entire loop immediately.
- **`continue`**: Skips only the current iteration and continues with the next one.

Both statements work with `for` and `while` loops in most programming languages (e.g., Python, Java, C++, JavaScript, etc.).
