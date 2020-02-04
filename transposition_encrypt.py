# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip


def main():
    my_message = 'Common sense is not so common.'
    my_key = 8

    cipher_text = encrypt_message(my_key, my_message)

    print(f'{cipher_text!r}')
    pyperclip.copy(cipher_text)


def encrypt_message(key, message):
    cipher_columns = [message[column::key] for column in range(key)]

    return ''.join(cipher_columns)


if __name__ == '__main__':
    main()

    print(repr(encrypt_message(9, 'Underneath a huge oak tree there was of'
                                  ' swine a huge company,')))
