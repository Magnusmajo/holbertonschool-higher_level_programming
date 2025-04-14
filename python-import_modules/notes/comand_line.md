# 10.3. Command Line Arguments

Utility scripts often need to handle command line arguments. These arguments are stored in the `sys` module’s `argv` attribute as a list. For example, consider the following `demo.py` file:

```python
# File: demo.py
import sys
print(sys.argv)
```

Running the script with `python demo.py one two three` at the command line produces the following output:

```python
['demo.py', 'one', 'two', 'three']
```

For more advanced command line argument parsing, the `argparse` module provides a robust solution. The script below demonstrates how to extract one or more filenames and an optional number of lines to display:

```python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file'
)
parser.add_argument('filenames', nargs='+', help='List of filenames')
parser.add_argument('-l', '--lines', type=int, default=10, help='Number of lines to display')
args = parser.parse_args()
print(args)
```

When executed with `python top.py --lines=5 alpha.txt beta.txt`, the script sets `args.lines` to `5` and `args.filenames` to `['alpha.txt', 'beta.txt']`.
