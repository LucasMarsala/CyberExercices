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


def perso_osint():
    s = "THISISASALT"
    cipher = "f23614e1c3bf8e2c6c30f3435f087df194795dfa674bf37a23e1578a0164a66c"
    dic = ["Athila", "athila", "Kita", "kita", "5", "Doggo", "doggo", "michel", "Michel", "Jacki", "jacki",
           "1", "8", "1989", "19", "89", "3", "Peter", "peter", "Amy", "amy", "12"
            "august", "August", "scotland", "Scotland", "!", "@", "-", "_", "&", ""]
            #"Giles", "giles", "United", "united", "kingdom", "Kingdom",
            #"December", "december", "Lane", "lane", "canterbury", "Canterbury", "kctf", "KCTF", ""]

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
                        for b in dic:
                            check_test(x + t + y + z + a + b + s, cipher)
                            check_test(t + x + y + z + a + b + s, cipher)
                            check_test(x + t + z + y + a + b + s, cipher)
                            check_test(t + x + z + y + a + b + s, cipher)
                            check_test(x + t + y + z + b + a + s, cipher)
                            check_test(t + x + y + z + b + a + s, cipher)
                            check_test(x + t + z + y + b + a + s, cipher)
                            check_test(t + x + z + y + b + a + s, cipher)
    print("The program could not find any matches")
    return 1


try:
    perso_osint()
except Exception:
    raise
