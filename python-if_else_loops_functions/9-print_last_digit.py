#!/usr/bin/python3

def print_last_digit(number):
    positive_number = abs(number)
    last_digit = positive_number % 10
    print(last_digit, end='')

    return(last_digit % 10)
