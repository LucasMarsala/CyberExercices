#!/usr/bin/env python3.9

def calculate_gcd(a, b):
    if b == 0:
        print("The GCD is ", a)
        exit(0)
    if (b > a):
        a, b = b, a
    calculate_gcd(b, (a % b))


try:
    print("Enter the first number")
    a = int(input())
    print("Enter the second number")
    b = int(input())

    if a < 0 or b < 0:
        print("Numbers should be positive")
        exit(0)
    else:
        calculate_gcd(a, b)
except Exception as e:
    print("You must give numbers")
    exit(0)
