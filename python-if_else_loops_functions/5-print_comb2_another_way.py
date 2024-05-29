#!/usr/bin/python3
"""
Prints the numbers 0 to 99, separated by < , >, followed by space
in ascendent order, with two digits
"""

print(', '.join(f"{i:02d}" for i in range(100)))
"""
the join function to concatenate a sequence of strings
The sequence is generated using a generator expression
The generator expression uses the range function to generate numbers from 0 to 99
The f-string formatting is used to convert each number to a two-digit string
"""
