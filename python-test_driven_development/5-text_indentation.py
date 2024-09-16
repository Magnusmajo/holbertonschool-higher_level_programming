#!/usr/bin/python3
"""Text indetation if any of ".", "?", ":", prints a New Line"""


def text_indentation(text):
    """If found any specified chars, add 2 New Line"""
    new_text = ""
    flag = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    if text == "":
        raise TypeError("text must be a string")
    new_text = text.replace(". ", ".")
    new_text = new_text.replace(": ", ":")
    new_text = new_text.replace("? ", "?")
    for char in new_text:
        if char in [".", "?", ":"]:
            print(char)
            print()
            flag = True
        else:
            if flag is False:
                print(char, end="")
            else:
                if char != " ":
                    print(char, end="")
                    flag = False
