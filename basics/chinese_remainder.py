#!/usr/bin/env python3.9

import math
from extended_euclidean import extended_euclidean



def chinese_remainder(a, M, b, N):
    values = []
    values = extended_euclidean(M, N)
    T = 0
    print("gcd(", M, ", ", N, ") = ", values[0], " = ", values[1], "*", M, " + ", values[2], "*", N ,sep='')
    for i in range (0, N):
        if (((i * M) % N) == 1):
            T = i
            break
    u = (((b - a) * T) % N)
    print("M' = ", values[1], ", T = ", T, "\nu = ", u, sep='')
    print("The solution for the two equations is:", (a + (u * M)))
    return (a + (u * M))

def main():
    try:
        print("Please enter the integer a: ", end='')
        a = int(input())
        print("Please enter the integer M: ", end='')
        M = int(input())
        if (M <= a):
            print("M should be greater than a")
            exit(1)
        print("Please enter the integer b: ", end='')
        b = int(input())
        print("Please enter the integer N: ", end='')
        N = int(input())
        if (N <= b):
            print("N should be greater than b")
            exit(1)
        elif ((N < 0) or (M < 0) or (b < 0) or (a < 0)):
            print("Numbers should be positive")
            exit(1)
        chinese_remainder(a, M, b, N)
    except Exception as e:
        raise
        exit(1)


if __name__ == "__main__":
    # execute only if run as a script
    main()
