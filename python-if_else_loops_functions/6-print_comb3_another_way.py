#!/usr/bin/python3
"""A program that prints all possible different combinations of two digits.

This program generates and prints all unique combinations of two digits, where
the digits are separated by a comma and a space. The combinations are printed
in ascending order, and only the smallest combination of two digits is printed.

The program uses the join function to concatenate a sequence of strings, which
are generated using a generator expression. The generator expression uses the
range function to generate numbers from 0 to 9, and f-string formatting is used
to convert each number to a two-digit string.

The program excludes the combination "89" from the output, as it is considered
the same as "98".
"""

print(', '.join(f"{i}{j}" if not (i == 8 and j == 9) else f"{i}{j}\n"
    for i in range(10) for j in range(i + 1, 10)))
