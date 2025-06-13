#!/usr/bin/env python3.9

import random
import math


''' calculate_legendre(i, p, quadratic)
    Checking if the value i mod p == 0
    Then return the value 0
    Checking if the value i mod p is in the quadratic residue of p.
    Then return 1
    Then return -1 which means i mod p is not in the quadratic residue of p
'''


def calculate_legendre(i, p, quadratic):

    if (i % p) == 0:
        return 0
    elif (i % p) in quadratic:
        return 1
    return -1


''' chinese_remainder(a, m, b, n)
    Setting the value t equals 0.
    Doing a loop from 0 to N.
    Checking if (i times m) mod n equals 1.
    Then setting the value of t equals 1. Breaking to get out of the loop.
    Setting the value u equals (((b - a) times t) mod n).
    Return the value (a + (u times m))
    Doing the algorithm seen in lecsem.
'''


def chinese_remainder(a, m, b, n):
    t = 0
    for i in range(0, n):
        if ((i * m) % n) == 1:
            t = i
            break
    u = (((b - a) * t) % n)
    return a + (u * m)


''' calculate_quadratic(p, q)
    Setting the value n which is p * q
    Setting an array named quadratic
    Doing a loop from 1 to N
    Setting the value check which is i to the power of 2 mod N
    Checking if the value check is already in the array named quadratic, if the condition is filled, skipping the 
    insertion of the value check.
    Otherwise, inserting the value of check in the quadratic array.
    Return the array named quadratic
'''


def calculate_quadratic(p, q):
    n = p * q
    quadratic = []
    for i in range(1, n + 1):
        check = ((i**2) % n)
        if check in quadratic:
            continue
        quadratic.append(check)
    return quadratic


''' calculate_non_quadratic(p, q)
    Getting the quadratic residue of p and q
    Setting the value n which p * q.
    Setting an array named non_quadratic.
    Doing a loop from 1 to N.
    If the value i is not in the quadratic residue.
    Inserting the value of i in the non quadratic residue array.
    Return the array named non_quadratic.
'''


def calculate_non_quadratic(p, q):
    quadratic = calculate_quadratic(p, q)
    n = p * q
    non_quadratic = []
    for i in range(1, n + 1):
        if i not in quadratic:
            non_quadratic.append(i)
    return non_quadratic


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
    for i in range(2, limit):
        if ((e * i) % limit) == 1:
            return i
    return -1


''' calculate_jacobi(p)
    Setting an array named jn. Jn which is the first and fourth quadrant seen in courses.
    Setting a value a equals to 0.
    Doing a loop from 0 to p. P is one of the composite number n which is p * q.
        Setting the value of i to i % p ?
        Setting the value t equals to 1.
            Doing another loop. While i is different from 0.
                Doing another loop inside. While (i mod 2) equals 0
                Setting the value of i to i / 2.
                Setting a value r equals to p % 8.
                Checking if r equals 3 or 5.
                Then setting the value of t to t times -1.
            Once the last loop is finished, swapping the value of i and p.
            Checking if i mod 4 equals 3 and p mod 4 equals 3.
            Then Setting the value of t to t times -1.
            Setting the value of i to i mod p.
        Checking if p == 1.
            Then inserting the value of a in the array named Jn.
        Setting the value of a to a + 1.
    Return the array named jn.
'''


def calculate_jacobi(p):
    jn = []
    a = 0
    for i in range(0, p):
        i = i % p
        t = 1
        while i != 0:
            while (i % 2) == 0:
                i = i / 2
                r = p % 8
                if (r == 3) or r == 5:
                    t = -1 * t
            i, p = p, i
            if ((i % 4) == 3) and ((p % 4) == 3):
                t = -1 * t
            i = i % p
        if p == 1:
            jn.append(a)
        a = a + 1
    return jn


''' display_encryption(key)
    Getting the bit to encrypt 0 or 1
    Checking if the bit entered is correct otherwise raise an error.
    Generating a random number x with the interval {2, N}
    Printing the ciphertext of the corresponding bit.
    Calling once again the choose_option function.
'''


def display_encryption(key):
    print("Encryption:\nYour message space is the set: {0, 1}\nPlease enter a number from this set: ", sep='', end='')
    message = int(input())
    if (message < 0) or (message > 1):
        raise Exception("Your message is not from the set.")
    x = generate_random_prime_with_interval(key[2])
    print("The ciphertext for your message ", message, " is ", (((key[3]**message) * (x**2)) % key[2]),
          "\n--------------------------------------------")
    choose_option(key)


''' display_decryption(key)
    Getting the ciphertext.
    Checking if the ciphertext is less than 1.
    Checking also if the ciphertext is not in the array of jacobi symbols. The jacobi symbols get all the values of a
    which are values equal to 1.
    Checking the value return by the legendre symbols. It's the only way to get back the encrypted bit. 
    If the value is -1, print the value 1
    Otherwise, print the value 0
'''


def display_decryption(key):
    print("Decryption:\nYour ciphertext space is the set J_N\nPlease enter a number from this set: ", sep='', end='')
    cipher = int(input())

    if (cipher < 0) or (cipher not in calculate_jacobi(key[2])):
        raise Exception("Your ciphertext is not from the set.")
    if calculate_legendre(cipher, key[0], calculate_quadratic(key[0], 1)) == -1:
        test = 1
    else:
        test = 0
    print("The plaintext for your ciphertext ", cipher, " is ", int(test),
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
        return -1
    if option == 1:
        return display_encryption(key)
    else:
        return display_decryption(key)


''' display_setup(nu)
    Generating a prime number p of nu/2 bits.
    Generating a prime number q of nu/2 bits.
    Set the variable limit which is ((p - 1) * (q - 1))
    Checking if p and q are different, otherwise generating another q prime number.
    Set n with p * q.
    Getting the non quadratic residue of p
    Getting the non quadratic residue of q
    Choosing a random number in the array of non quadratic residue of p.
    Choosing a random number in the array of non quadratic residue of q.
    Getting the value y which is the chinese remainder of y = yp mod p and y = yq mod q.
    Displaying the first prime number p.
    Displaying the second primer number q.
    Displaying the integer N which is p times q.
    Displaying the public key y.
    Return an array of these values, p, q, n, y.
'''


def display_setup(nu):
    print("--------------------------------------------\nSetup:")
    p = generate_random_prime(math.ceil((nu / 2)))
    q = generate_random_prime(math.ceil((nu / 2)))
    while q == p:
        q = generate_random_prime(math.ceil((nu / 2)))
    n = p * q
    non_quadratic_p = calculate_non_quadratic(p, 1)
    non_quadratic_q = calculate_non_quadratic(q, 1)
    yp = non_quadratic_p[random.randint(0, len(non_quadratic_p) - 1)]
    yq = non_quadratic_q[random.randint(0, len(non_quadratic_q) - 1)]
    y = chinese_remainder(yp, p, yq, q)
    print("The first prime generated by the Setup algorithm is p =", p)
    print("The second prime generated by the Setup algorithm is q =", q)
    print("The integer N = pq =", n)
    print("The public key y =", y)
    print("--------------------------------------------")
    return [p, q, n, y]


''' main()
    This is the main function of the program, this is where everything start.
    Getting the nu parameter.
    Checking if nu is greater than or equal to 32. It means generating prime number p and q of 16 bits long.
    Moreover, without external libraries, it could take several hours to generate random number and checking is 
    they are prime. Also, checking if nu is greater than 4. Generating number under 4 bits numbers leads to 
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
