# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import os
import time

import transposition_decrypt
import transposition_encrypt


def main(input_filename, my_key, my_mode):
    if not os.path.exists(input_filename):
        raise OSError(f'The file {input_filename!r} does not exist.')

    with open(input_filename) as input_file:
        content = input_file.read()

    print(f'{my_mode.title()}ing...')

    start_time = time.time()
    if my_mode == 'encrypt':
        translated = transposition_encrypt.encrypt_message(my_key, content)
    elif my_mode == 'decrypt':
        translated = transposition_decrypt.decrypt_message(my_key, content)
    else:
        raise ValueError(f"Unexpected my_mode: {my_mode!r}"
                         f" (must be 'encrypt' or 'decrypt')")
    total_time = round(time.time() - start_time, 2)
    print(f'{my_mode.title()}ion time: {total_time} seconds')

    stem, suffix = os.path.splitext(input_filename)
    output_filename = f'{stem}_{my_mode}ed{suffix}'

    with open(output_filename, 'w') as output_file:
        output_file.write(translated)

    print(f'Done {my_mode}ing {input_filename!r} ({len(content)} characters).')
    print(f'{my_mode.title()}ed file is {output_filename!r}.')


if __name__ == '__main__':
    main('frankenstein.txt', 10, 'encrypt')
