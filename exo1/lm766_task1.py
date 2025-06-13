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
    for i in range(2, sqrt + 1):
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


''' generate_random_prime(bits)
    Using getrandbits to generate a number of nu/2 bits. 
    Checking if the number generated is a prime number.
    If the condition is filled, i'm returning the number.
    Otherwise i'm calling the function until the condition is reached.
'''


def generate_random_prime(bits: int):
    n = random.getrandbits(bits)
    if is_prime(n) == 1:
        return n
    return generate_random_prime(bits)


''' find_inverse(e, limit)
    I'm not using extended_euclidean algorithm because in some cases, mine doesn't work.
    Moreover, this is the easiest way to find the inverse of exponent e. The number generated is named i.
    I'm checking all the numbers between 2 and the limit ((p - 1) * (q - 1)) to find the inverse.
    If (e * i) modulo the limit equals 1, then the number i is the inverse of e. 
    Otherwise, i'm returning -1 if it doesn't find any number. It means that there is a problem in my program.
    Even if this is not the best way to find it, we are checking for 32 bits maximum number. Nowadays, computers can 
    check them quickly. It doesn't impact very munch the efficiency of this program.
'''


def find_inverse(e, limit):
    for i in range(2, limit + 1):
        if ((e * i) % limit) == 1:
            return i
    return -1


''' display_encryption(key)
    Display the space between of the set N. From 0 to N - 1.
    Set a value selected from the user from this set.
    Check if that value is in the set.
    Display the encryption of this message. Using (message * e) mod N.
    Call once again choose_option function
'''


def display_encryption(key):
    print("Encryption:\nYour message space is the set {Z/NZ} = {0, 1, ..., ", key[2] - 1,
          "}\nPlease enter a number from this set: ", sep='', end='')
    message = int(input())

    if (message < 0) or (message > (key[2] - 1)):
        raise Exception("Your message is not from the set.")
    print("The ciphertext for your message ", message, " is ", ((message ** key[3]) % key[2]),
          "\n--------------------------------------------")
    choose_option(key)


''' display_decryption(key)
    Display the space between of the set N. From 0 to N - 1.
    Set a value selected from the user from this set.
    Check if that value is in the set.
    Display the decryption of this ciphertext. Using (cipher * d) mod N.
    Call once again choose_option function
'''


def display_decryption(key):
    print("Decryption:\nYour ciphertext space is the set {Z/NZ} = {0, 1, ..., ", key[2] - 1,
          "}\nPlease enter a number from this set: ", sep='', end='')
    cipher = int(input())

    if (cipher < 0) or (cipher > (key[2] - 1)):
        raise Exception("Your ciphertext is not from the set.")
    print("The plaintext for your ciphertext ", cipher, " is ", ((cipher ** key[4]) % key[2]),
          "\n--------------------------------------------")
    choose_option(key)


''' choose_option(key)
    Display the option part of the program where user can choose between decryption, encryption and quit.
    If a value different from 1 or 2 is chosen, the program quit.
    If 1 is chosen, the encryption part function is called.
    If 2 is chosen, the decryption part function is called.
'''


def choose_option(key):
    print("Please enter an option:\n1 to Encrypt\n2 to Decrypt\nAny other number to quit\nYour option: ", end='')
    option: int = int(input())
    print("--------------------------------------------")
    if (option > 2) or (option < 1):
        return 0
    if option == 1:
        display_encryption(key)
    else:
        display_decryption(key)


''' display_setup(nu)
    Generating a prime number p of nu/2 bits.
    Generating a prime number q of nu/2 bits.
    Set the variable limit which is ((p - 1) * (q - 1))
    Checking if p and q are different, otherwise generating another q prime number.
    Checking if limit is equals 2. If limit equals 2, generating the exponent e is impossible. 
    1 < e < 2 with gcd(e, 2) == 1. That's why, 'nu' should be greater than 4.
    Then generating another q, to get another limit.
    Set n with p * q.
    Generating e with the limit.
    Generating d which is the inverse of e. e and d can be equals here, even if it can lead to a breach. I didn't 
    want to change it to get a minimum value of 5 for 'nu'. 
    If the inverse of e could not be found, there is an error in the program.
    Displaying the values of p, q, n, e and d.
    Return an array of these values, p, q, n, e, d.
'''


def display_setup(nu):
    print("--------------------------------------------\nSetup:")
    p = generate_random_prime(math.ceil((nu / 2)))
    q = generate_random_prime(math.ceil((nu / 2)))
    limit = ((p - 1) * (q - 1))
    while (q == p) or (limit == 2):
        q = generate_random_prime(math.ceil((nu / 2)))
        limit = (p - 1) * (q - 1)
    n = p * q
    e = generate_random_prime_with_interval(limit)
    d = find_inverse(e, limit)
    if d == -1:
        raise Exception("Did not find the inverse of e")
    print("The first prime generated by the Setup algorithm is p =", p)
    print("The second prime generated by the Setup algorithm is q =", q)
    print("The integer N = pq =", n)
    print("The encryption exponent is e =", e)
    print("The decryption exponent is d =", d)
    print("--------------------------------------------")
    return [p, q, n, e, d]


''' main()
    This is the main function of the program, this is where everything start.
    Getting the nu parameter.
    Checking if nu is greater than or equal to 32. It means generating prime number p and q of 16 bits long.
    Moreover, without external libraries, it could take several hours to generate random number and checking is 
    they are prime. Also, checking if nu is greater than 3. Generating number under 4 bits numbers leads to 
    p/q = nu/2 bits numbers which means that p or q are 1 bits numbers. This is impossible to generate 
    two different prime numbers.
    Calling the display_setup function and giving the nu parameter.
    It's return an array with all the variables i need to encrypt/decrypt.
    Calling the choose_option function and giving the array of variables to decrypt/encrypt.
'''


def main():
    try:
        print("Please enter the security parameter 'nu': ", end='')
        nu = int(input())
        if nu < 5 or nu >= 32:
            raise Exception("'nu' should be 5 <= 'nu' < 32, cannot generate nu/2-bits number and keep RSA secure")
        key = display_setup(nu)
        return choose_option(key)
    except Exception:
        raise


''' set a special variable named main
    calling the main function
'''


if __name__ == "__main__":
    main()
