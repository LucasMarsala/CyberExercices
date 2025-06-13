#!/usr/bin/env python3.9

import hashlib


def login():
    print("Username: ", end='')
    u = input()
    print("Password: ", end='')
    p = input()
    f = open("database_1.txt", "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        data = line.split(";")
        if data[0] == u:
            password = p + data[1]
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


try:
    login()
except Exception:
    raise
