import os

import pytest

from transposition_file_cipher import translate_file


@pytest.mark.parametrize('name', ('frankenstein',
                                  'romeo_and_juliet',
                                  'the_time_machine'))
@pytest.mark.parametrize('key', (10, 645, 3507, 69528))
def test_transposition_file_cipher(name, key):
    translate_file(f'{name}.txt', key, 'encrypt')
    translate_file(f'{name}_encrypted.txt', key, 'decrypt')

    with open(f'{name}.txt') as original_file, \
            open(f'{name}_encrypted_decrypted.txt') as roundtrip_file:
        assert original_file.read() == roundtrip_file.read()

    os.remove(f'{name}_encrypted.txt')
    os.remove(f'{name}_encrypted_decrypted.txt')
