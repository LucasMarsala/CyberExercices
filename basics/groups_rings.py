#!/usr/bin/env python3.9

tab_add = []
tab_prime = []

def display_addition_table(N):
    print("\nDisplay of the additon table of N = ", N)
    print(N, "| ", end='')
    for i in range (0, N):
        print(i, end = ' ')
    print('')
    for i in range (0, N):
        print('--', end = '-')
    for y in range (0, N):
        print()
        print(y, end = ' ')
        print('| ', end = '')
        for x in range (0, N):
            tab_add.append((x + y) % N)
            print((x + y) % N, end = ' ')
    print()

def display_multiplication_table_of_prime_numbers(tab_prime, N):
    print("\nDisplay of the multiplication table of N = ", N, " with the prime numbers")
    print(N, "| ", end='')
    for i in range (0, len(tab_prime)):
        print(tab_prime[i], end = ' ')
    print('')
    for i in range (0, len(tab_prime)):
        print('--', end = '-')
    for y in range (0, len(tab_prime)):
        print()
        print(tab_prime[y], end = ' ')
        print('| ', end = '')
        for x in range (0, len(tab_prime)):
            print((tab_prime[x] * tab_prime[y]) % N, end = ' ')
    print()

def find_the_mutually_prime_numbers(N):
    print()
    for y in range (1, N):
        for x in range (1, N):
            if ((x * y) % N == 1):
                tab_prime.append(y)
    print("The numbers which are mutually prime in the set of N = ", N, " are ", tab_prime)


def display_ka_values(N):
    print("\nDisplay the values of ka with 1 <= k <= |Z/NZ|")
    for y in range (0, N):
        print()
        print(y, end = ' ')
        print('| ', end = '')
        for x in range (0, N):
            print((y * (x + 1)) % N, end = ' ')
    print()

def display_ka_values_of_primes_numbers(tab_prime, N):
    print("\nDisplay the values of a to the power of i with 1 <= i <= |Z/NZ|*")
    for y in range (0, len(tab_prime)):
        print()
        print(tab_prime[y], end = ' ')
        print('| ', end = '')
        for x in range (0, len(tab_prime)):
            print((tab_prime[y] ** (x + 1)) % N, end = ' ')
    print()

try:
    print("Enter the first number")
    N = int(input())
    if N < 0 :
        print("Numbers should be positive")
        exit(0)
    display_addition_table(N)
    display_ka_values(N)
    find_the_mutually_prime_numbers(N)
    display_ka_values_of_primes_numbers(tab_prime, N)
    display_multiplication_table_of_prime_numbers(tab_prime, N)

except Exception as e:
    print("You must give numbers")
    raise
    exit(0)
