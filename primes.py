import math
import random


def is_prime_trial_div(num):
    if num < 2:
        return False

    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False

    return True


def prime_sieve(size):
    sieve = [True] * size
    sieve[:2] = [False, False]

    for n in range(2, math.isqrt(size) + 1):
        if not sieve[n]:
            continue
        for multiple in range(n * 2, size, n):
            sieve[multiple] = False

    return [n for n, _is_prime in enumerate(sieve) if _is_prime]


LOW_PRIMES = prime_sieve(100)


def rabin_miller(num):
    if num % 2 == 0 or num < 2:
        return False
    if num == 3:
        return True

    s = num - 1
    t = 0
    while s % 2 == 0:
        s //= 2
        t += 1
    for _ in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != num - 1:
                if i == t - 1:
                    return False
                else:
                    i += 1
                    v = v**2 % num
    return True


def is_prime(num):
    if num < 2:
        return False
    if num in LOW_PRIMES:
        return True
    for prime in LOW_PRIMES:
        if num % prime == 0:
            return False

    return rabin_miller(num)


def generate_large_prime(key_size=1024):
    while True:
        num = random.randrange(2**(key_size - 1), 2**key_size)
        if is_prime(num):
            return num
