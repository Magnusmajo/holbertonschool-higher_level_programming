#!usr/bin/python3
"""
A program to print the alphabet in lowercase, not followed by
a new line. 
"""

print(''.join(chr(i) for i in range(97, 123)))
"""
It takes an integer in range 97 to 123, wich is the ASCII alphabet,
then convert the integers in characterswith chr(i), and then with
the method < .join > all those char ar joined in the same line.

Output:
abcdefghijklmnopqrstuvwxyz
"""