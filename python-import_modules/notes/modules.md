### 6. Modules

When you exit the Python interpreter, any definitions you’ve made (functions, variables, etc.) are lost. To create longer programs, it’s better to use a text editor to write your code and run it as a script. For larger programs, splitting them into multiple files makes maintenance easier. Python allows you to reuse functions across multiple programs without copying their definitions by using **modules**.

A **module** is a file containing Python definitions and statements, with a `.py` extension. You can import these modules into other scripts or interactive sessions. For example, create a file `fibo.py` with the following content:

```python
# Fibonacci numbers module

def fib(n):    # Write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # Return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

You can import this module in Python:

```python
import fibo
```

This adds the module name `fibo` to your namespace. Access its functions using the module name:

```python
fibo.fib(1000)
fibo.fib2(100)
fibo.__name__
```

To use a function frequently, assign it to a local name:

```python
fib = fibo.fib
fib(500)
```

---

### 6.1. More on Modules

Modules can include executable statements for initialization, which run only the first time the module is imported. Each module has its own private namespace, avoiding conflicts with other modules or scripts.

#### Import Variants

- Import specific functions or variables:

  ```python
  from fibo import fib, fib2
  fib(500)
  ```

- Import all names (not recommended for readability):

  ```python
  from fibo import *
  ```

- Use aliases for modules or functions:

  ```python
  import fibo as fib
  from fibo import fib as fibonacci
  ```

#### Reloading Modules

To reload a module during an interactive session:

```python
import importlib
importlib.reload(fibo)
```

---

### 6.1.1. Executing Modules as Scripts

Run a module as a script using:

```bash
python fibo.py <arguments>
```

Add the following to make the module executable as a script:

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

---

### 6.1.2. The Module Search Path

When importing a module, Python searches:

1. The directory of the script.
2. Directories in `PYTHONPATH`.
3. Default installation paths.

Modify the search path using:

```python
import sys
sys.path.append('/path/to/directory')
```

---

### 6.1.3. “Compiled” Python Files

Python caches compiled modules in `__pycache__` for faster loading. These files are platform-independent but must match the source file’s modification date. Use the `compileall` module to precompile files.

---

### 6.2. Standard Modules

Python includes a library of standard modules. For example, the `sys` module provides access to interpreter variables like `sys.ps1` and `sys.path`.

---

### 6.3. The `dir()` Function

Use `dir()` to list names defined in a module:

```python
import fibo
dir(fibo)
```

Without arguments, `dir()` lists names in the current namespace. To see built-in names, use:

```python
import builtins
dir(builtins)
```
