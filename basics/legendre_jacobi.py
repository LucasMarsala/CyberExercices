#!/usr/bin/env python3.9

import math

def calculate_legendre(i, p, quadric):

    if (i % p) == 0:
        print("0", sep='', end='')
    elif (i % p) in quadric:
        print("1", sep='', end='')
    elif (i % p) not in quadric:
        print("-1", sep='', end='')
    return 0


def calculate_jacobi(i, p):
    i = i % p
    t = 1
    while i != 0:
        while (i % 2) == 0:
            i = i / 2
            r = p % 8
            if (r == 3) or r == 5:
                t = -1 * t
        i, p = p, i
        if ((i % 4) == 3) and ((p % 4) == 3):
            t = -1 * t
        i = i % p
    if p == 1:
        return t
    return 0

def main():
    try:
        print("Please enter the prime p: ", end='')
        p = int(input())
        print("Please enter the prime q: ", end='')
        q = int(input())
        if (q <= 0 or p <= 0):
            print("Numbers should be positive")
            exit(1)
        n = p * q
        print("N =", n, "\n-------------------------------------")
        print("a\t(a/", p, ")\t(a/", q,")\t(a/", n,")\n-------------------------------------", sep='')
        quadric = []
        for i in range (1, n):
            check = ((i**2) % n)
            if check in quadric:
                continue
            quadric.append(check)
        for i in range (0, n):
            print(i, "\t", end='', sep='')
            calculate_legendre(i, p, quadric)
            print("\t", end='', sep='')
            calculate_legendre(i, q, quadric)
            print("\t", end='', sep='')
            print(calculate_jacobi(i, n), end='')
            print("")
        print("\n-------------------------------------")
    except Exception as e:
        raise
        exit(1)


if __name__ == "__main__":
    # execute only if run as a script
    main()
