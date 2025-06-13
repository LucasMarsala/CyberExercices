#!/usr/bin/env python3.9

import math
from partial_trial_division import partial_trial_division

def prime_factorisation(n):
    primes = []
    temp = n
    i = 2

    while (temp != 1 and i <= n):
        if (((temp % i) == 0) and partial_trial_division(i, int(math.sqrt(i)) == 1)):
            primes.append(i)
            temp = int(temp / i)
            i = i - 1
        i = i + 1
    print("The prime factorisation of ", n, " is: ", sep='', end='')
    i = 0
    while (i < len(primes)):
        if (primes.count(primes[i]) > 1):
            print(primes[i], "^", primes.count(primes[i]), sep='', end='')
            i = i + primes.count(primes[i]) - 1
        else:
            print(primes[i], sep='', end='')
        if (i == len(primes) - 1):
            break
        print(" * ", sep='', end='')
        i = i + 1

def main():
    try:
        print("Please enter the interger n: ", end='')
        n = int(input())

        if (n < 0):
            print("N should be a positive number")
            exit(1)
        if (partial_trial_division(n, int(math.sqrt(n))) == 1):
            print(n, " is a prime number.", sep='', end='')
        else:
            prime_factorisation(n)
    except Exception as e:
        raise
        exit(1)


if __name__ == "__main__":
    # execute only if run as a script
    main()
