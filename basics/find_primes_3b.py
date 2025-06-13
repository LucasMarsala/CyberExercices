#!/usr/bin/env python3.9

import math
from partial_trial_division import partial_trial_division


def Fermat_test(n, k):
    a = 101
    for i in range (0, k):
        if (((a**(n - 1)) % n) != 1):
            return a
        a = a + 1
    return 1

def main():
    try:
        print("Please enter the interger n: ", end='')
        n = int(input())
        print("Please enter the number of iterations k: ", end='')
        k = int(input())

        if ((n < 0) or (k < 1)):
            print("N should be positive")
            exit(1)
        print("Searching for divisors only among primes between 2 and 97")
        print("Running Fermat's test for k = ", k, " iterations", sep='')
        if (partial_trial_division(n, 97) == 1 and Fermat_test(n, k) == 1):
                print("The number ", n, " is probably prime (verified with partial trial division with prime numbers less than 100 and with Fermat's test with ", k, " iterations).", sep='')
        else:
            print("The number ", n, " is composite with the certificate of compositeness being ", Fermat_test(n, k), "." , sep='')
    except Exception as e:
        raise
        exit(1)


if __name__ == "__main__":
    # execute only if run as a script
    main()
