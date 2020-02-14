from transposition_file_cipher import translate_file


def test_transposition_file_cipher():
    translate_file('frankenstein.txt', 10, 'encrypt')
    translate_file('frankenstein_encrypted.txt', 10, 'decrypt')

    with open('frankenstein.txt') as original_file, \
            open('frankenstein_encrypted_decrypted.txt') as roundtrip_file:
        assert original_file.read() == roundtrip_file.read()
