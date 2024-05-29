#!usr/bin/python3
"""
A function that prints  all numbers from 0 to 98 in decimal and in hexadecimal
"""


print('\n'.join(f"{i} = 0x{i:x}" for i in range(98)))
"""
In this code < f"{i} = 0x{i:x}" > is an string that converts < i >
into decimal format. The < :x > is a format specifier that converts
the number into hexadecimal format. The < f > before the string is a
format specifier that allows us to embed expressions inside string
the bucle for iterates from 0 to 98,
and < '\n'.join() > concatenates all strings with a line break between them.
"""
