#!/usr/bin/env python3.9


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


''' display_encryption(n, d)
    Getting the message decrypted by task1
    Checking if the plaintext m' is less than 1 to raise an error.
    Displaying (the plaintext m' times the inverse of 2) mod N. 
'''


def display_decryption(n, d):
    print("Please decrypt the modified ciphertext c' using your program from Task 1.")
    print("Please input the plaintext m' decrypted from c': ", end='')
    message = int(input())
    if message < 1:
        raise Exception("Your message should be greater than or equal to one.")
    print("The original plaintext message m computed from m' is:", ((d*message) % n))
    print("-----------------------------------------")


''' display_cca(n, e, c)
    Displaying the new ciphertext c' which is 2 times ciphertext.
    Displaying the inverse of 2.
'''


def display_cca(n, e, c):
    print("The modified  ciphertext c' is = ", (((2**e)*c) % n), end='')
    print("\nThe inverse of 2 mod ", n, " is = ", find_inverse(2, n), end='')
    print("\n-----------------------------------------")
    display_decryption(n, find_inverse(2, n))


''' display_setup()
    Getting the parameter N
    Getting the parameter e
    Checking if the public key values are less than 1 to raise an error.
    Getting the ciphertext c.
'''


def display_setup():
    print("Please enter the public parameter N: ", end='')
    n = int(input())
    print("Please enter the encryption exponent e: ", end='')
    e = int(input())
    if n < 1 or e < 1:
        raise Exception("N or e should greater than or equal to one.")
    print("-----------------------------------------\nPlease enter the ciphertext c: ", end='')
    c = int(input())
    print("-----------------------------------------")
    display_cca(n, e, c)


''' main()
    calling the display_setup function
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
