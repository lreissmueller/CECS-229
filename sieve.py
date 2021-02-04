'''
 This program uses the sieve of Eratosthenes to find all primes less than 10,000 by deleting all multiples of a known prime.
 @ author Luke, Reissmueller
 @ 10/21/2020
 @ sieve.py

'''
from math import *


def sieve(integer):

    nums = [True for i in range(integer + 1)]

    nums[0] = False
    nums[1] = False

    for i in range(2, int(sqrt(integer)) + 1):
        if nums[i]:
            for n in range(i * 2, integer + 1, i):
                nums[n] = False

    nums_end = []
    for i, flag in enumerate(nums):
        if flag:
            nums_end.append(i)
    print(nums_end)
