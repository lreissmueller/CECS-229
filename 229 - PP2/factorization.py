'''
 This program finds all of the positive divisors of a positive integer from its prime factorization.
 @ author Luke, Reissmueller
 @ 10/21/2020
 @ factorization.py

'''

def factorization(integer):

    nums = []
    i = 2
    integer = int(integer)
    while i < integer:
        if integer % i == 0 and integer != i:
            integer /= i
            if isPrime(int(i)):
                nums.append(int(i))
            if isPrime(int(integer)):
                nums.append((int(integer)))
                break
            i = 2
        else:
            i += 1
    print(nums)



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

