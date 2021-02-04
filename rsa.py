

'''
 This program generates valid keys (e, n) for the RSA cryptosystem where n = p(prime) * q(prime) and e = (p-1)*(q-1) which is co-prime to n.
 @ author Luke, Reissmueller
 @ 10/21/2020
 @ rsa.py

'''


def rsa(p, q):
    p = int(p)
    q = int(q)
    n = p * q
    e = (p - 1) * (q - 1)
    if gcd(n, e) == 1:
        print(n, e)

def isPrime(num):
    flag = True
    if num == 1:
        return False
    for i in range(2, num):
        if num == 2:
            return True
        if num % i == 0:
            return False
    return flag

def gcd(a, b):  # Uses Euclidean Algorithm to find greatest common divisor of two positive integers
    x = a
    y = b
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

