#!/usr/bin/env python3.9


import random
import math


''' calculate_gcd(a, b)
    I'm checking if b is greater than a. If it is, then i'm swapping the two variables.
    I'm always working on b < a to be sure that the recursive works.
    While b is different from 0, i'm calling the function.
    I'm giving a the value of b and b the value (a modulo b) to reach 0.
    If b equals 0, then i'm returning a which is the gcd of a and b.
'''


def calculate_gcd(a, b):
    if b == 0:
        return a
    if b > a:
        a, b = b, a
    return calculate_gcd(b, (a % b))


''' is_prime(n)
    If the parameter n is 1, it could be consider as a prime number because it pass through the condition loop. 
    Using math.sqrt to get the square_root of the parameter n. It's give a limit to check if n is a prime or not.
    From 2 to the square_root of n, i'm testing all the numbers to check if one of them can divide n.
    If one of them can divide n, then n is not a prime, otherwise n is a prime.
'''


def is_prime(n):
    if n < 2:
        return 0
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt):
        if (n % i) == 0:
            return 0
    return 1


''' generate_random_prime_with_interval(limit)
    I'm using this function to generate a prime from the interval {2, ..., ((p - 1) * (q - 1))} for the exponent e.
    I'm checking if the number generated is mutually prime to ((p - 1) * (q - 1)) and if it's a prime number.
    If both conditions are filled, i'm returning the number n.
    Otherwise i'm calling the function until both conditions are reached
'''


def generate_random_prime_with_interval(limit):
    n = random.randint(2, limit)
    if (calculate_gcd(n, limit) == 1) and (is_prime(n) == 1):
        return n
    return generate_random_prime_with_interval(limit)


''' display_cca(n, c)
    Getting a random prime number in the interval {2, N}
    Displaying the ciphertext c' which is (z² times ciphertext) mod N.
'''


def display_cca(n, c):
    z = generate_random_prime_with_interval(n)
    print("The modified  ciphertext c' is = ", (((z**2)*c) % n), end='')
    print("\n-----------------------------------------")


''' display_setup()
    Getting the public parameter N
    Getting the encryption key y
    Checking if the public key values are less than 1 to raise an error.
    Getting the ciphertext c.
    Calling the display_cca function
'''


def display_setup():
    print("Please enter the public parameter N: ", end='')
    n = int(input())
    print("Please enter the encryption key y: ", end='')
    y = int(input())
    if n < 1 or y < 1:
        raise Exception("N or e should greater than or equal to one.")
    print("-----------------------------------------\nPlease enter the ciphertext c: ", end='')
    c = int(input())
    print("-----------------------------------------")
    display_cca(n, c)


''' main()
    Calling the display_setup function
'''


def main():
    try:
        display_setup()
    except Exception:
        raise


''' set a special variable named main
    calling the main function
'''


if __name__ == "__main__":
    main()
