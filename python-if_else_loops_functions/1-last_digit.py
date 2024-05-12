#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
is_digit = abs(num) % 10

if is_digit < 0:
    is_digit = -is_digit
    print(f"Last digit of {} is {} and is ".format(num, is_digit), end="")
if is_digit > 5:
    print(f"Last digit of {number} is {is_digit} and is greater than 5")
elif is_digit == 0:
    print(f"Last digit of {number} is {is_digit} and is 0")
else:
    print(f"Last digit of {number} is {is_digit} and is less than 6 and not 0")
