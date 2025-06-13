#!/usr/bin/env python3.9

import hashlib


def check_test(test, cipher):
    if hashlib.sha1(test.strip().encode()).hexdigest() == cipher:
        print("The password is", test.strip(), "using sha1.")
        exit(0)
    elif hashlib.sha256(test.strip().encode()).hexdigest() == cipher:
        print("The password is", test.strip(), "using sha256.")
        exit(0)
    elif hashlib.sha512(test.strip().encode()).hexdigest() == cipher:
        print("The password is", test.strip(), "using sha512.")
        exit(0)
    return 1


def perso_dico():
    s = "5UA@/Mw^%He]SBaU"
    cipher = "3281e6de7fa3c6fd6d6c8098347aeb06bd35b0f74b96f173c7b2d28135e14d45"
    dic = ["laplusbelle", "Laplusbelle", "Woof", "woof", "Eltrofor", "eltrofor", "Marie", "marie", "jean", "Jean",
            "Jvaist", "jvaist", "Neoskour", "neoskour", "Fairecourir", "fairecourir", "UKC", "ukc", "Curie", "curie",
            "Kent", "kent", "Canterbury", "canterbury", "university", "University", "29", "2", "twenty nine", "two",
            "12",  "1", "01", "twelve", "Twelve", "one", "One", "January", "january", "December", "december",
            "80", "81", "1980", "1981", "eighty", "eighty one", "nineteen eighty", "nineteen eighty one", ""]

    for x in dic:
        check_test(x + s, cipher)
        for t in dic:
            check_test(x + t + s, cipher)
            check_test(t + x + s, cipher)
            for y in dic:
                check_test(x + t + y + s, cipher)
                check_test(t + x + y + s, cipher)
                for z in dic:
                    check_test(x + t + y + z + s, cipher)
                    check_test(t + x + y + z + s, cipher)
                    check_test(x + t + z + y + s, cipher)
                    check_test(t + x + z + y + s, cipher)
                    for a in dic:
                        check_test(x + t + y + z + a + s, cipher)
                        check_test(t + x + y + z + a + s, cipher)
                        check_test(x + t + z + y + a + s, cipher)
                        check_test(t + x + z + y + a + s, cipher)
    print("The program could not find any matches")
    return 1


try:
    perso_dico()
except Exception:
    raise
