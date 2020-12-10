#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    sum = 0
    length = len(args)
    for n in range(1, length):
        sum += int(args[n])
    print(sum)
