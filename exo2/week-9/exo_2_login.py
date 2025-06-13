#!/usr/bin/env python3.9

import hashlib
from exo_2_register import generate_hash_from_file


def login(u, p):
    print("Username: ", u)
    print("Path to your file as password: ", p)
    f = open("database_2.txt", "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        data = line.split(";")
        if data[0] == u:
            password = generate_hash_from_file(p) + data[1]
            cipher = hashlib.sha256(password.encode()).hexdigest()
            cipher = hashlib.sha256(cipher.encode()).hexdigest()
            if cipher == data[2]:
                print("Successfully logged in")
                return 0
            else:
                print("Error with your username or password")
                return 1
    print("Error with your username or password")
    return 1


if __name__ == "__main__":
    try:
        login()
    except Exception:
        raise
