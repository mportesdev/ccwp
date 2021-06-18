import math
from itertools import zip_longest


def encrypt(key, message):
    # key == number of columns
    return ''.join(message[column::key]
                   for column in range(key))


def decrypt(key, message):
    # key == number of columns
    num_rows = math.ceil(len(message) / key)
    num_blank_cells = num_rows * key - len(message)

    # how many values are in columns without a blank cell
    n = num_rows * (key - num_blank_cells)
    part_1 = message[:n]
    part_2 = message[n:]

    # transpose first part with stride=num_rows
    part_1 = [part_1[row::num_rows] for row in range(num_rows)]

    # transpose second part with stride=num_rows-1
    part_2 = [part_2[row::num_rows - 1] for row in range(num_rows - 1)]

    return ''.join(s1 + s2
                   for s1, s2 in zip_longest(part_1, part_2, fillvalue=''))
