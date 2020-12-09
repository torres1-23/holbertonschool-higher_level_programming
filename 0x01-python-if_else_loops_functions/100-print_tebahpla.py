#!/usr/bin/python3
for n in range(ord("z"), ord("a") - 1, -1):
    if n % 2 == 0:
        letter = chr(n)
    else:
        letter = chr(n - (ord("a") - ord("A")))
    print(letter, end="")
