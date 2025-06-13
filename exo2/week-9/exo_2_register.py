#!/usr/bin/env python3.9

import string
import random
import hashlib


def salt_generator(size=1000, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_hash_from_file(path):
    file_hash = hashlib.sha256()
    with open(path, 'rb') as f:
        fb = f.read(65536)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(65536)
    return file_hash.hexdigest()


def register(u, p):
    print("Username: ", u)
    print("Path of a file for your password: ", p)
    s = salt_generator()
    new_pass = generate_hash_from_file(p) + s
    cipher = hashlib.sha256(new_pass.encode()).hexdigest()
    cipher = hashlib.sha256(cipher.encode()).hexdigest()
    f = open("database_2.txt", "a+")
    f.seek(0)
    lines = f.readlines()
    for line in lines:
        data = line.split(";")
        if data[0] == u:
            pass_test = generate_hash_from_file(p) + data[1]
            cipher_test = hashlib.sha256(pass_test.encode()).hexdigest()
            cipher_test = hashlib.sha256(cipher_test.encode()).hexdigest()
            if data[2] == cipher_test:
                raise Exception("user already exist")
        else:
            data.clear()
    if len(lines) > 0:
        f.write('\n')
    f.write(u + ";" + s + ";" + cipher + ";")
    f.close()


if __name__ == "__main__":
    try:
        register()
    except Exception:
        raise
