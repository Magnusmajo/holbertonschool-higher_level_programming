# The return statements

## Return Value of a Function Without a `return` Statement

In Python, when a function doesn't have an explicit `return` statement, it automatically returns the special value `None`. This is Python's way of representing the absence of a value.

---

### Key Points

#### Implicit Return

```python
def no_return_function():
    print("This function doesn't have a return statement")

result = no_return_function()
print(result)  # Output: None
```

#### Empty Return

Even if you just write `return` without a value, it returns `None`:

```python
def empty_return_function():
    print("This function has an empty return")
    return

result = empty_return_function()
print(result)  # Output: None
```

---

### Why This Matters

- You might accidentally get `None` when you expected something else.
- It's important when chaining function calls.
- Many built-in methods (like `list.append()`) return `None`.

---

### Practical Implications

```python
def add_numbers(a, b):
    a + b  # Oops - forgot to return!

sum_result = add_numbers(2, 3)
print(sum_result)  # Output: None (not 5 as you might expect)
```

---

### Checking for `None`

```python
def might_return_something(flag):
    if flag:
        return "Something"
    # implicit None return if flag is False

value = might_return_something(False)
if value is None:
    print("Got no value back")
```

---

### Remember

`None` is different from:

- `False` (a boolean value)
- `0` (a numeric value)
- An empty string/container (`""`, `[]`, `{}`)

It is a specific singleton object in Python that represents "no value."
