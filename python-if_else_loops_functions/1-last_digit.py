#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number % 10
if number > 0:
    print(f"Las digit of {number} is {n} and is greater than 5")
elif number == 0:
    print(f"Las digit of {number} is {n} and is 0")
else:
    print(f"Las digit of {number} is {n} and is less than 6 and not 0")
