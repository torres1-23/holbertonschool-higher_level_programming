#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    sum = 0
    for n in range(1, len(args)):
        sum += int(args[n])
    print(sum)
