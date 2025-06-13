#!/usr/bin/env python3.9

import math


def partial_trial_division(n, k):
    sqrt = int(math.sqrt(n))
    for i in range (2, k + 1):
        if ((n % i) == 0):
            return 0
    return 1
