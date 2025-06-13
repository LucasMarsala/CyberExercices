#!/usr/bin/env python3.9


def calculate_lcm(p, q):
    tab = []
    res = 1
    val = list(set(p + q))

    for i in range(0, len(val)):
        if p.count(val[i]) > q.count(val[i]):
            tab.append(val[i] ** p.count(val[i]))
        else:
            tab.append(val[i] ** q.count(val[i]))
    for i in range(0, len(tab)):
        res = res * tab[i]
    return res