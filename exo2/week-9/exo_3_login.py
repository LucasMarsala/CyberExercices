#!/usr/bin/env python3.9

import hashlib
from datetime import datetime


def generate_otp(password):
    test = hashlib.sha256(password.encode()).hexdigest()
    return test[-6: len(test)]


def login():
    print("Username: ", end='')
    u = input()
    print("Password: ", end='')
    p = input()
    f = open("database_3.txt", "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        data = line.split(";")
        if data[0] == u:
            password = p + data[1]
            cipher = hashlib.sha256(password.encode()).hexdigest()
            cipher = hashlib.sha256(cipher.encode()).hexdigest()
            if cipher == data[2]:
                time = datetime.now()
                print("Your generated code is ", generate_otp(data[2] + str(time)))
                
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
