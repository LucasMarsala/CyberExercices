#!/usr/bin/env python3.9

import hashlib


def dictionary_attack():
    print("Enter a hash: ", end='')
    cipher = input()
    f = open("phpbb.txt", "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        if hashlib.sha1(line.strip().encode()).hexdigest() == cipher:
            print("The password is", line.strip(), "using sha1.")
            return 0
        elif hashlib.sha256(line.strip().encode()).hexdigest() == cipher:
            print("The password is", line.strip(), "using sha256.")
            return 0
        elif hashlib.sha512(line.strip().encode()).hexdigest() == cipher:
            print("The password is", line.strip(), "using sha512.")
            return 0
    print("The program could not find any matches")
    return 1


try:
    dictionary_attack()
except Exception:
    raise
