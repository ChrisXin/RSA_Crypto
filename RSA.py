#!/usr/bin/env python3
import random
import math


# modular exponentiation
def modexp(x, e, N):
    """
    Input: Three positive integers x and e, and N.
    Output: The number x^e mod N
    """
    if e == 0:
        return 1
    z = modexp(x, e // 2, N)
    if e % 2 == 0:
        return z * z % N
    else:
        return x * z * z % N


# for extended Euclid
def extended_euclid(a, b):
    """
    Input: Two positive integers a >= b >= 0
    Output: Three integers x, y, and d returned as a tuple (x, y, d) 
            such that d = gcd(a, b) and ax + by = d
    """
    if b == 0:
        return 1, 0, a
    d, e, f = extended_euclid(b, a % b)
    return e, d - (a//b) * e ,f


def primality(N):
    """
    Test if a number N is prime using Fermat's little Theorem with
    ten random values of a.  If a^(N-1) mod N = 1 for all values,
    then return true.  Otherwise return false.
    Hint:  you can generate a random integer between a and b using
    random.randint(a,b).
    """
    i = 0
    while i < 10:
        a = random.randint(0, N-1)
        if modexp(a, N-1, N) % N != 1:
            return False
        i += 1
    return True


def prime_generator(N):
    """
    This function generates a prime number <= N
    """
    a = random.randint(0, N)
    while not(primality(a)):
        a = random.randint(0, N)
    return a


def main():
    """
    Test file for the two parts of the question
    """
    ## Excercise 1:  generating primes and RSA
    ##################
    p = prime_generator(10000000) #6345839
    q = prime_generator(10000000) #8546933
    N = p * q
    e = 5
    x = 329415
    print("p: ", p) #6345839
    print("q: ", q) #8546933

    ##################
    print("extended_euclid(e, (p-1)*(q-1))", extended_euclid(e, (p-1)*(q-1)))
    #print("extended_euclid(e, (p-1)*(q-1))", extended_euclid(3,6))
    d = extended_euclid(e, (p-1)*(q-1))[0] #43389956695213

    ##################
    print("N", N)
    encodedMessage = modexp(329415, e, N)
    print("encoded message x^e mod N: ", encodedMessage)
    print('decoded message encodedMessage^d mod N', modexp(encodedMessage, d, N))

if __name__ == '__main__':
    main()
