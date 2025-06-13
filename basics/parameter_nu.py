#!/usr/bin/env python3.9

import sys

def print_numbers_between_zero_and_n(n):

    for i in range (0, n):
        print(i)

def main():
    try:
        if (len(sys.argv) != 2):
            print("The program need one argument which is the paramater v")
            exit(1)
        v = int(sys.argv[1])
        if (v <= 0):
            print("v should be a positive number")
            exit(1)
        print_numbers_between_zero_and_n(2**v)
    except Exception as e:
        raise
        exit(1)


if __name__ == "__main__":
    # execute only if run as a script
    main()
