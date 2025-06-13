#!/usr/bin/env python3.9

import math

primes = []
inverse = []

def use_extended_euclidean(a, b):
    r = b
    r1 = a
    s = 0
    s1 = 1
    t = 1
    t1 = 0
    values = []
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
    if (((values[1] * a) + (values[2] * b)) == 1):
        primes.append(b)

def find_inverse(a, N):
    for i in range (0, N):
        if (((a * i) % N) == 1):
            inverse.append(i)
def main():
    try:
        print("Please enter the prime p: ", end='')
        p = int(input())
        print("Please enter the prime q: ", end='')
        q = int(input())
        N = p * q
        values = []
        if (p < 0) or (q < 0):
            print("Numbers should be positive")
            exit(1)
        print("-------------------------------\nThe elements of (Z/", N, "Z)* and their respective inverses are:", sep='')
        for i in range (1, N):
            use_extended_euclidean(N, i)
            find_inverse(i, N)
        for i in range (0, len(primes)):
            print(primes[i], "with the inverse =", inverse[i])
        print("-------------------------------\nphi(N) = ", len(primes), " is the number of elements in (Z/", N, "Z)*\n-------------------------------\nAll the values of a^(phi(N)):", sep='')
        for i in range (0, N):
            print(i, "^", len(primes), " = ", ((i**len(primes)) % N), sep='')
        print("-------------------------------\n")
    except Exception as e:
        raise
        exit(1)


if __name__ == "__main__":
    # execute only if run as a script
    main()
