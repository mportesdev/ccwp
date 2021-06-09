from primes import is_prime_trial_div, prime_sieve, is_prime

import pytest


@pytest.mark.parametrize(
    'num, expected',
    (
        (1, False),
        (2, True),
        (4, False),
        (521, True),
        (521 ** 2, False),
    )
)
def test_is_prime_trial_div(num, expected):
    assert is_prime_trial_div(num) is expected


@pytest.mark.parametrize(
    'size, expected',
    (
        (1, []),
        (2, []),
        (3, [2]),
        (9, [2, 3, 5, 7]),
        (50, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]),
    )
)
def test_prime_sieve(size, expected):
    assert prime_sieve(size) == expected


@pytest.mark.parametrize(
    'num, expected',
    (
        (1, False),
        (2, True),
        (4, False),
        (686863, True),
        (686863 ** 2, False),
    )
)
def test_is_prime(num, expected):
    assert is_prime(num) is expected
