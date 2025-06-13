#!/usr/bin/env python3.9

import math
from partial_trial_division import partial_trial_division
from legendre_jacobi_usefull import *
from prime_factorisation import prime_factorisation

def main():
    try:
        print("Please enter the interger a: ", end='')
        a = int(input())
        print("Please enter the interger n: ", end='')
        n = int(input())
        primes = []
        quadratic = []
        if ((n < 0) or (a < 0) and (n > 10000) or (a > 10000)):
            print("Numbers should be positive")
            exit(1)
        primes = prime_factorisation(n)
        i = 0
        while (i < len(primes)):
            quadratic = calculate_quadratic(a, primes[i])
            if (primes.count(primes[i]) > 1):
                print("(", a, "/", primes[i], ")^", primes.count(primes[i]), " = ", calculate_jacobi(a, primes[i], quadratic), "^", primes.count(primes[i])," = " , calculate_jacobi(a, primes[i], quadratic)**primes.count(primes[i]), sep='')
                i = i + primes.count(primes[i]) - 1
            else:
                print("(", a, "/", primes[i], ")^1", " = ", calculate_jacobi(a, primes[i], quadratic), "^1", " = " , calculate_jacobi(a, primes[i], quadratic)**primes.count(primes[i]), sep='')
            if (i == len(primes) - 1):
                break
            i = i + 1
        print("Jacobi symbol: ", calculate_jacobi(a, n, quadratic))
    except Exception as e:
        raise
        exit(1)


if __name__ == "__main__":
    # execute only if run as a script
    main()
