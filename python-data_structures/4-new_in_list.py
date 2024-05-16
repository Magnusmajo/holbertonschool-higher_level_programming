#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """deletes the element at index
    idx in a list of integers and replaces it"""
    kopiereen = list(my_list)
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    kopiereen[idx] = element
    return kopiereen
