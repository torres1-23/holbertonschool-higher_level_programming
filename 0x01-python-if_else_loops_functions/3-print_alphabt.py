#!/usr/bin/python3
letter = ord("a")
while letter <= ord("z"):
    if letter != ord("q") and letter != ord("e"):
        print(chr(letter), end="")
    letter += 1
