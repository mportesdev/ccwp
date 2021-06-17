from pathlib import Path

import pytest

from transposition import encrypt, decrypt


@pytest.mark.parametrize(
    'message, key, expected',
    (
        ('Common sense is not so common.', 8, 'Cenoonommstmme oo snnio. s s c'),
        ('Then they trotted away for the wind grew high: One acorn they left,'
         ' and no more might you spy.',
         9,
         'T atg:renishtwhr nfogperaeeO t hynoy wnt,mt. t w eh o ttfih earyheoni'
         'ayneoedrdgc d uy   hol m '),
    )
)
def test_encrypt(message, key, expected):
    assert encrypt(key, message) == expected


@pytest.mark.parametrize(
    'message, key, expected',
    (
        ('Cenoonommstmme oo snnio. s s c', 8, 'Common sense is not so common.'),
        ('T atg:renishtwhr nfogperaeeO t hynoy wnt,mt. t w eh o ttfih earyheoni'
         'ayneoedrdgc d uy   hol m ',
         9,
         'Then they trotted away for the wind grew high: One acorn they left,'
         ' and no more might you spy.'),
    )
)
def test_decrypt(message, key, expected):
    assert decrypt(key, message) == expected


@pytest.mark.parametrize('filename', ('frankenstein.txt',
                                      'the_time_machine.txt'))
@pytest.mark.parametrize('key', (10, 645, 3507))
def test_file_roundtrip(filename, key):
    original = Path(filename).read_text()
    round_trip = decrypt(key, encrypt(key, original))
    assert original == round_trip
