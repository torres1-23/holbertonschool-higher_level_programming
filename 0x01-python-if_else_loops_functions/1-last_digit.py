#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if ld > 5:
    str = "and is greater than 5"
elif ld < 6 and ld != 0:
    str = "and is less than 6 and not 0"    
else:
    str = "and is 0"
print("Last digit of {:d} is {:d} {}".format(number, ld, str))
