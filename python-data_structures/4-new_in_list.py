#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """deletes the element at index idx in a list of integers and replaces it"""
    if idx < 0 or idx >= len(my_list):
        return my_list.copy
    kopiereen = my_list.copy()
    kopiereen[idx] = element
    return kopiereen

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)