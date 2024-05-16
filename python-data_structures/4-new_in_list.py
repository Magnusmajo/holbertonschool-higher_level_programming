#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """deletes the element at index idx in a list of integers and replaces it"""
    kopiereen = my_list
    kopiereen[idx] = element
    if idx < 0 or idx >= len(my_list):
        return my_list.copy
    return kopiereen
