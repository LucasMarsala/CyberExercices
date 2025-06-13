#!/usr/bin/env python3.9

import math

def calculate_legendre(i, p, quadratic):

    if ((i % p) == 0):
        return 0
    elif ((i % p) in quadratic):
        return 1
    elif ((i % p) not in quadratic):
        return -1
    return 0


def calculate_jacobi(i, p, quadratic):
    i = i % p
    t = 1
    while (i != 0):
        while ((i % 2) == 0):
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

def calculate_quadratic(p, q):
    n = p * q
    quadratic = []
    for i in range (1, n):
        check = ((i**2) % n)
        if (check in quadratic):
            continue
        quadratic.append(check)
    return quadratic

def initialisation_jacobi_legendre(p, q):
    try:
        if (q <= 0 or p <= 0):
            print("Numbers should be positive")
            exit(1)
        n = p * q
        quadratic = []
        for i in range (1, n):
            check = ((i**2) % n)
            if (check in quadratic):
                continue
            quadratic.append(check)
        for i in range (0, n):
            calculate_legendre(i, p, quadratic)
            calculate_legendre(i, q, quadratic)
            print(calculate_jacobi(i, n, quadratic), end='')
    except Exception as e:
        raise
        exit(1)


if __name__ == "__main__":
    # execute only if run as a script
    main()
