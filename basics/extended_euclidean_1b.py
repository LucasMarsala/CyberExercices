#!/usr/bin/env python3.9



primes = []

def use_extended_euclidean(a, b):
    r = b
    r1 = a
    s = 0
    s1 = 1
    t = 1
    t1 = 0
    q = 0
    values = []
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
    print("gcd(", a, ", ", b, ") = ", ((values[1] * a) + (values[2] * b)), " = ", values[1], "*", a, " + ", values[2], "*", b, sep='')
    if (((values[1] * a) + (values[2] * b)) == 1):
        print("(inverse of ", b, " = ", b, ")", sep='')
        primes.append(b)
    return primes


def main():
    try:
        print("Please enter the interger N: ", end='')
        N = int(input())

        if (N < 0) :
            print("N should be positive")
            exit(1)
        for i in range (1, N):
            use_extended_euclidean(N, i)
        print("\n(Z/", N, "Z)* = ", primes, sep='')
    except Exception as e:
        raise
        exit(1)

if __name__ == "__main__":
    # execute only if run as a script
    main()
