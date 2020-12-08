#!/usr/bin/python3
for n in range(0, ((ord("z") - ord("a")) + 1)):
    if (ord("a") + n) != ord("q") and (ord("a") + n) != ord("e"):
        print("{}".format(chr(ord("a") + n)), end="")
