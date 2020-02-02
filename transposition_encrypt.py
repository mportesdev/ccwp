# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip


def main():
    my_message = 'Common sense is not so common.'
    my_key = 8

    cipher_text = encrypt_message(my_key, my_message)

    print(repr(cipher_text))
    pyperclip.copy(cipher_text)


def encrypt_message(key, message):
    cipher_columns = [message[column::key] for column in range(key)]

    return ''.join(cipher_columns)


if __name__ == '__main__':
    main()
