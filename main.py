from rsa import rsa
from rsa import isPrime
from sieve import sieve
from factorization import factorization
import random

'''
 This program is the main method which contains all of the methods and their demos. 
 @ author Luke, Reissmueller
 @ 10/21/2020
 @ main.py

'''

option = ''
while option != '0':
    option = input('''
    1) Generate valid keys (e,n) for the RSA cryptosystem.
    2) Use the Sieve of Eratosthenes to find all primes less than 10,000(or in this case the user can choose).
    3) Find all of the positive divisors of a positive integer from its prime factorization.
    ''')

    if option == '1':
        p = random.randint(1, 10000000)
        q = random.randint(1, 10000000)
        while not (isPrime(p) and isPrime(q)):
            p = random.randint(1, 10000000)
            q = random.randint(1, 10000000)
        rsa(p, q)
    elif option == '2':
        o = int(input('Enter positive integer to be sieved.'))
        sieve(o)
    elif option == '3':
        o = int(input('Enter positive integer for prime factorization.'))
        factorization(o)

print('Come again.')