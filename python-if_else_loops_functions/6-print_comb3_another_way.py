#!/usr/bin/python3
"""
program that prints all possible different combinations of two digits.
Numbers must be separated by ,, followed by a space
The two digits must be different
01 and 10 are considered the same combination of the two digits 0 and 1
Print only the smallest combination of two digits
Numbers should be printed in ascending order, with two digits
"""

print(', '.join(f"{i}{j}" if not (i == 8 and j == 9) else f"{i}{j}\n" \
    for i in range(10) for j in range(i + 1, 10)))
"""
Use the join function to concatenate a sequence of strings
The sequence is generated using a generator expression
The generator expression uses the range function to generate numbers from 0 to 99
The f-string formatting is used to convert each number to a two-digit string
"""
