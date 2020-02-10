# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import random
import sys

import transposition_decrypt
import transposition_encrypt


def main():
    random.seed(42)

    for i in range(20):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        message = list(message)

        random.shuffle(message)
        message = ''.join(message)

        print(f'Test #{i + 1}: {message[:50]!r}')

        for key in range(1, len(message) // 2):
            encrypted = transposition_encrypt.encrypt_message(key, message)
            decrypted = transposition_decrypt.decrypt_message(key, encrypted)

            if message != decrypted:
                print(f'Mismatch with key {key} and message {message!r}.')
                print(f'Decrypted as: {decrypted!r}')
                sys.exit()

    print('Transposition cipher test passed.')


if __name__ == '__main__':
    main()
