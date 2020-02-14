import pytest

from transposition_file_cipher import translate_file


@pytest.mark.parametrize('name', ('frankenstein',
                                  'romeo_and_juliet',
                                  'the_time_machine'))
def test_transposition_file_cipher(name):
    translate_file(f'{name}.txt', 10, 'encrypt')
    translate_file(f'{name}_encrypted.txt', 10, 'decrypt')

    with open(f'{name}.txt') as original_file, \
            open(f'{name}_encrypted_decrypted.txt') as roundtrip_file:
        assert original_file.read() == roundtrip_file.read()
