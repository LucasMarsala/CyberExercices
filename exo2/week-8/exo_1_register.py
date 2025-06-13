#!/usr/bin/env python3.9

import string
import random
import hashlib


def salt_generator(size=1000, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def register():
    print("Username: ", end='')
    u = input()
    print("Password: ", end='')
    p = input()
    print("Additional information: ", end='')
    pi = input()
    s = salt_generator()
    new_pass = p + s
    cipher = hashlib.sha256(new_pass.encode()).hexdigest()
    cipher = hashlib.sha256(cipher.encode()).hexdigest()
    f = open("database_1.txt", "w")
    f.write(u + ";" + s + ";" + cipher + ";" + pi)
    f.close()


try:
    register()
except Exception:
    raise
