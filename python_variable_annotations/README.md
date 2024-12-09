# Python - Variable Annotations

Variable annotations in Python are a way to provide type hints for variables. They were introduced in PEP 526 and allow developers to specify the expected data type of a variable. This can improve code readability and help with static type checking. Annotations do not affect the runtime behavior of the code but can be used by tools like type checkers, IDEs, and linters to catch potential type errors.

Key points:
- Introduced in Python 3.6 via PEP 526.
- Syntax: `variable_name: type = value`.
- Used for type hinting and static type checking.
- Enhances code readability and maintainability.
- Supported by tools like mypy, PyCharm, and VS Code.

Example:
```python
age: int = 25
name: str = "Alice"
height: float = 5.9
```
