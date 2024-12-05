# Explanation of Python's Small Integer Caching

In Python, small integers (typically between -5 and 256) are cached and shared. This means that when we assign `a = 1` and `b = 1`, both `a` and `b` refer to the same object in memory. Therefore, `a is b` will evaluate to `True`.

Even though we initially provided an example with a tuple `(1)`, in this specific example with integers `a` and `b`, the same principle applies.

If we want to ensure `a` and `b` are distinct objects, we can assign them larger or different values, or we can use other types of objects such as lists or tuples.