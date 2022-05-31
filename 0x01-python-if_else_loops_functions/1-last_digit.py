#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

Last_d = abs(number) % 10

if number < 0:
    Last_d = -(Last_d)

if Last_d > 5:
    print(f"last digit of {number:d} is {Last_d} and is greater than 5")

if Last_d == 0:
    print(f"Last digit of {number:d} is {Last_d} and is 0")

if Last_d < 6 != 0:
    print(f"Last digit of {number:d} is {Last_d} and is less than 6 and not 0")
