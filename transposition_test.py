# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import random
from string import ascii_uppercase
import sys

from transposition import encrypt, decrypt


def main():
    random.seed(42)

    for i in range(20):
        message_letters = random.choices(ascii_uppercase,
                                         k=random.randint(100, 1000))
        message = ''.join(message_letters)

        print(f'Test #{i + 1}: {message[:50]!r}')

        for key in range(1, len(message) // 2):
            encrypted = encrypt(key, message)
            decrypted = decrypt(key, encrypted)

            if message != decrypted:
                print(f'Mismatch with key {key} and message {message!r}.')
                print(f'Decrypted as: {decrypted!r}')
                sys.exit()

    print('Transposition cipher test passed.')


if __name__ == '__main__':
    main()
