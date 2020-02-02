# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip


def main():
    my_message = 'Common sense is not so common.'
    my_key = 8

    cipher_text = encrypt_message(my_key, my_message)

    print(repr(cipher_text))
    pyperclip.copy(cipher_text)


def encrypt_message(key, message):
    cipher_columns = [''] * key

    for column in range(key):
        current_index = column

        while current_index < len(message):
            cipher_columns[column] += message[current_index]
            current_index += key

    return ''.join(cipher_columns)


if __name__ == '__main__':
    main()
