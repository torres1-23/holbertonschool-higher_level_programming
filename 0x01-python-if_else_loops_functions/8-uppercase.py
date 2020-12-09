#!/usr/bin/python3
def uppercase(str):
    for n in range(len(str)):
        if ord(str[n]) >= ord("a") and ord(str[n]) <= ord("z"):
            tmp = chr(ord(str[n]) - (ord("a") - ord("A")))
        else:
            tmp = str[n]
        print(tmp, end="")
    print()
