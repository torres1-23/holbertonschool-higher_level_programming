#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    length = len(sys.argv)
    if length == 2:
        print("1 argument:\n1: {}".format(args[1]))
    elif length > 2:
        print("{:d} arguments:".format(length - 1))
        for n in range(1, length):
            print("{:d}: {}".format(n, args[n]))
    else:
        print("0 arguments.")
