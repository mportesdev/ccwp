import os
from pathlib import Path

import pytest

from transposition import encrypt, decrypt
from transposition_file_cipher import translate_file


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


@pytest.mark.parametrize('name', ('frankenstein', 'the_time_machine'))
@pytest.mark.parametrize('key', (10, 645, 3507))
def test_transposition_file_cipher(name, key):
    translate_file(f'{name}.txt', key, 'encrypt')
    translate_file(f'{name}_encrypted.txt', key, 'decrypt')

    original_file = Path(f'{name}.txt')
    roundtrip_file = Path(f'{name}_encrypted_decrypted.txt')
    assert original_file.read_text() == roundtrip_file.read_text()

    os.remove(f'{name}_encrypted.txt')
    os.remove(f'{name}_encrypted_decrypted.txt')
