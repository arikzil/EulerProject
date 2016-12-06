'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''


def is_prime(num):
    total = 1

    for i in range(2, num + 1):

        if num % i == 0:
            total += 1

    return total == 2

