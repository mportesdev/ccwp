import random
import math

from crypto_utils import find_mod_inverse
from primes import generate_large_prime


def generate_keys(key_size):
    while True:
        p = generate_large_prime(key_size)
        q = generate_large_prime(key_size)
        if p != q:
            break

    while True:
        e = random.randrange(2 ** (key_size - 1), 2 ** key_size)
        if math.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    n = p * q
    public_key = n, e

    d = find_mod_inverse(e, (p - 1) * (q - 1))
    private_key = n, d

    return public_key, private_key
