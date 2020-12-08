#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
ld_abs = abs(ld)
if ld_abs > 5:
    str = "and is greater than 5"
elif ld_abs == 0:
    str = "and is 0"
else:
    str = "and is less than 6 and not 0"
print("Last digit of {:d} is {:d} {}".format(number, ld, str))
