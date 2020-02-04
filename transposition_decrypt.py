# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import math

import pyperclip


def main():
    my_message = 'Cenoonommstmme oo snnio. s s c'
    my_key = 8

    plaintext = decrypt_message(my_key, my_message)

    print(f'{plaintext!r}')
    pyperclip.copy(plaintext)


def decrypt_message(key, message):
    num_of_columns = math.ceil(len(message) / key)
    num_of_rows = key
    shaded_boxes = num_of_columns * num_of_rows - len(message)

    plaintext = [''] * num_of_columns

    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        if column == num_of_columns or (column == num_of_columns - 1 and
                                        row >= num_of_rows - shaded_boxes):
            column = 0
            row += 1

    return ''.join(plaintext)


if __name__ == '__main__':
    main()

    print(repr(decrypt_message(9, 'Uhot  on ahoamdakef pe  r harhtesunnur'
                                  ' wgyegewie,aeean t  sec')))

    print(repr(decrypt_message(9, 'H cb  irhdeuousBdi   prrtyevdgp nir  '
                                  'eerit eatoreechadihf paken ge b te dih aoa.'
                                  'da tts tn')))
