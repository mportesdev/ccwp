# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import os
import sys
import time

import transposition_decrypt
import transposition_encrypt


def main():
    input_filename = 'frankenstein.txt'
    output_filename = 'frankenstein.encrypted.txt'
    my_key = 10
    my_mode = 'encrypt'

    if not os.path.exists(input_filename):
        print(f'The file {input_filename!r} does not exist. Quitting...')
        sys.exit()

    if os.path.exists(output_filename):
        print(f'This will overwrite the file {output_filename!r}.'
              ' (C)ontinue or (Q)uit?')
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    file_obj = open(input_filename)
    content = file_obj.read()
    file_obj.close()

    print(f'{my_mode.title()}ing...')

    start_time = time.time()
    if my_mode == 'encrypt':
        translated = transposition_encrypt.encrypt_message(my_key, content)
    elif my_mode == 'decrypt':
        translated = transposition_decrypt.decrypt_message(my_key, content)
    total_time = round(time.time() - start_time, 2)
    print(f'{my_mode.title()}ion time: {total_time} seconds')

    output_file_obj = open(output_filename, 'w')
    output_file_obj.write(translated)
    output_file_obj.close()

    print(f'Done {my_mode}ing {input_filename} ({len(content)} characters).')
    print(f'{my_mode.title()}ed file is {output_filename}.')


if __name__ == '__main__':
    main()
