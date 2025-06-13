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
    i = 0
    while (i < len(primes)):
        if (primes.count(primes[i]) > 1):
            i = i + primes.count(primes[i]) - 1
        if (i == len(primes) - 1):
            break
        i = i + 1
    return primes
