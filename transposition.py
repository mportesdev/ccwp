import math


def encrypt_message(key, message):
    cipher_columns = [message[column::key] for column in range(key)]

    return ''.join(cipher_columns)


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
