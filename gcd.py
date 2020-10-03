# Luke Reissmueller
# CECS 229 - Programming Assignment 1
# 9/18/2020

# gcd function
def gcd(a, b):  # Uses Euclidean Algorithm to find greatest common divisor of two positive integers
    x = a
    y = b
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

print(gcd(1760, 1840))  # Test gcd, returns 30
