#!/usr/bin/python3
for i in range(97,123):
    print(chr(i), end="")
"""
A more elegant way:
print(*(chr(i) for i in range(97,123)), sep="")

- * (unpacking operator): The asterisk before the generator expression unpacks the elements of the generated sequence, passing each character as a separate argument to the print function.
- sep="": This argument of the print function specifies that the elements should be printed without any separator between them. By default, print separates elements with a space, but using sep="" ensures that the characters are printed one after another without spaces.
- chr(i) for i in range(97,123): This generator expression generates characters corresponding to ASCII values in the range 97 to 122, which represent lowercase letters 'a' to 'z'."""
