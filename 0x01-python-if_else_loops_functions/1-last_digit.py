#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

Last_digit = number % 10 

if Last_digit > 5:
    print(f"last digit of {number:d} is {Last_digit} and is greater than 5")

if Last_digit ==  0: 
    print(f"Last digit of {number:d} is {Last_digit} and is 0")

if Last_digit <  6 != 0: 
    print(f"Last digit of {number:d} is {Last_digit} and is  less than 6 and not 0")

