# Arithmetic Operators in Python

Python provides several arithmetic operators for performing mathematical operations. Here's a complete guide to using them:

## Basic Arithmetic Operators

### 1. Addition (`+`)

```python
x = 5 + 3   # x = 8
print(2.5 + 1.5)  # 4.0
print("Hello" + " " + "World")  # String concatenation: "Hello World"
```

### 2. Subtraction (`-`)

```python
y = 10 - 4  # y = 6
print(-5)   # Unary minus: -5
```

### 3. Multiplication (`*`)

```python
z = 3 * 4    # z = 12
print(2.5 * 3)  # 7.5
print("Hi" * 3)  # String repetition: "HiHiHi"
```

### 4. Division (`/`)

Always returns a float (even when dividing integers).

```python
a = 10 / 2  # a = 5.0
b = 9 / 4   # b = 2.25
```

### 5. Floor Division (`//`)

Returns the largest integer less than or equal to the result.

```python
c = 10 // 3  # c = 3 (not 3.333)
d = -5 // 2  # d = -3 (rounds toward negative infinity)
```

### 6. Modulus (`%`)

Returns the remainder after division.

```python
e = 10 % 3  # e = 1
f = 15 % 4  # f = 3
```

### 7. Exponentiation (`**`)

```python
g = 2 ** 3   # g = 8 (2 to the power of 3)
h = 16 ** 0.5  # h = 4.0 (square root)
```

---

## Operator Precedence

Python follows standard mathematical precedence:

1. **Parentheses** `()` (highest precedence)
2. **Exponentiation** `**`
3. **Unary plus/minus** `+x`, `-x`
4. **Multiplication, Division, Floor Division, Modulus** `*`, `/`, `//`, `%`
5. **Addition and Subtraction** `+`, `-` (lowest precedence)

---

## Compound Assignment Operators

Combine arithmetic with assignment:

```python
x = 5
x += 3   # Equivalent to x = x + 3 → 8
x -= 2   # x = x - 2 → 6
x *= 4   # x = x * 4 → 24
x /= 3   # x = x / 3 → 8.0
x //= 5  # x = x // 5 → 1.0
x **= 3  # x = x ** 3 → 1.0
x %= 2   # x = x % 2 → 0.0
```

---

## Special Cases and Tips

- **Division by zero** raises `ZeroDivisionError`.

- **Mixed-type operations**: Python automatically converts to the more complex type.

    ```python
    print(5 + 2.5)  # int + float → float (7.5)

    ```

- **Complex numbers** use `j` notation:

    ```python
    z = 3 + 4j
    print(z * 2)  # (6+8j)
    ```

- **Bitwise operators** are different (`&`, `|`, `^`, `~`, `<<`, `>>`).

---

## Practical Examples

### Calculate the area of a circle

```python
radius = 5
area = 3.14159 * radius ** 2
```

### Convert seconds to minutes and seconds

```python
total_seconds = 135
minutes = total_seconds // 60
seconds = total_seconds % 60
print(f"{minutes}m {seconds}s")  # "2m 15s"
```

### Check if a number is even

```python
num = 7
if num % 2 == 0:
        print("Even")
else:
        print("Odd")
```
