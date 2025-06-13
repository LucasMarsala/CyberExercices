#!/usr/bin/env python3.9


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
