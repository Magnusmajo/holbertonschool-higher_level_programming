#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_int = set()
    sum = 0
    for num in my_list:
        if num not in uniq_int:
            sum += num
            uniq_int.add(num)
    return sum
