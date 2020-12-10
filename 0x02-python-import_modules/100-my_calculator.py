#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    args = sys.argv
    length = len(args)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(args[1])
        b = int(args[3])
        if args[2] == "+":
            print("{:d} + {:d} = {:d}".format(a, b, calculator_1.add(a, b)))
        elif args[2] == "-":
            print("{:d} - {:d} = {:d}".format(a, b, calculator_1.sub(a, b)))
        elif args[2] == "*":
            print("{:d} * {:d} = {:d}".format(a, b, calculator_1.mul(a, b)))
        elif args[2] == "/":
            print("{:d} / {:d} = {:d}".format(a, b, calculator_1.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
