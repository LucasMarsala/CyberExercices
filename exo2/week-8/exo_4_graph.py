#!/usr/bin/env python3.9


import hashlib


def check_test(test, cipher):
    if hashlib.sha1(test.strip().encode()).hexdigest() == cipher:
        print("The password is", test.strip(), "using sha1.")
        exit(0)
    return 1


def break_graph():
    cipher = "91077079768edba10ac0c93b7108bc639d778d67"
    pattern = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    for x in pattern:
        check_test(x, cipher)
        for y in pattern:
            if y == x:
                continue
            check_test(x + y, cipher)
            for z in pattern:
                if z == x or z == y:
                    continue
                check_test(x + y + z, cipher)
                for a in pattern:
                    if a == x or a == y or a == z:
                        continue
                    check_test(x + y + z + a, cipher)
                    for b in pattern:
                        if b == x or b == y or b == z or b == a:
                            continue
                        check_test(x + y + z + a + b, cipher)
                        for c in pattern:
                            if c == x or c == y or c == z or c == a or c == b:
                                continue
                            check_test(x + y + z + a + b + c, cipher)
                            for d in pattern:
                                if d == x or d == y or d == z or d == a or d == b or d == c:
                                    continue
                                check_test(x + y + z + a + b + c + d, cipher)
                                for f in pattern:
                                    if f == x or f == y or f == z or f == a or f == b or f == c or f == d:
                                        continue
                                    check_test(x + y + z + a + b + c + d + f, cipher)
                                    for g in pattern:
                                        if g == x or g == y or g == z or g == a or g == b or g == c or g == d or g == f:
                                            continue
                                        check_test(x + y + z + a + b + c + d + f + g, cipher)
    print("Could not find any matches")
    return 1


def main():
    try:
        break_graph()
    except Exception:
        raise


if __name__ == "__main__":
    # execute only if run as a script
    main()
