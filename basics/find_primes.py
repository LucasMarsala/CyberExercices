#!/usr/bin/env python3.9

import math


def extended_euclidean(a, b):
    values = []
    r = b
    r1 = a
    s = 0
    s1 = 1
    t = 1
    t1 = 0
    q = 0
    while (r != 0):
        values.clear()
        q = int(r1 / r)
        temp = (r1 - (q * r))
        r1 = r
        r = temp
        temp = (s1 - (q * s))
        s1 = s
        s = temp
        temp = (t1 - (q * t))
        t1 = t
        t = temp
        values.append(r1)
        values.append(s1)
        values.append(t1)
    return values


def find_primes(n):
    sqrt = int(math.sqrt(n))
    print("Searching for divisors between 2 and ", sqrt, ".", sep='')
    for i in range(2, sqrt + 1):
        if ((n % i) == 0):
            print("The number ", n, " is a composite with the certificate of compositeness being ", sqrt, ".", sep='')
            return 0
    print("The number", n, "is a prime.")
    return 1


def main():
    try:
        print("Please enter the interger n: ", end='')
        n = int(input())

        if n < 0:
            print("N should be positive")
            exit(1)
        find_primes(n)
    except Exception:
        raise


if __name__ == "__main__":
    # execute only if run as a script
    main()
