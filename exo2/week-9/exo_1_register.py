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
    f = open("database_1.txt", "a+")
    f.seek(0)
    lines = f.readlines()
    for line in lines:
        data = line.split(";")
        if data[0] == u:
            pass_test = p + data[1]
            cipher_test = hashlib.sha256(pass_test.encode()).hexdigest()
            cipher_test = hashlib.sha256(cipher_test.encode()).hexdigest()
            if data[2] == cipher_test:
                raise Exception("user already exist")
        else:
            data.clear()
    if len(lines) > 0:
        f.write('\n')
    f.write(u + ";" + s + ";" + cipher + ";" + pi)
    f.close()


try:
    register()
except Exception:
    raise
