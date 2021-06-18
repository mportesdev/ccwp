import math
from pathlib import Path
from string import ascii_letters


def find_mod_inverse(a, m):
    if math.gcd(a, m) != 1:
        return

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q*v1), (u2 - q*v2), (u3 - q*v3), \
            v1, v2, v3

    return u1 % m


LETTERS_AND_SPACE = ascii_letters + ' \t\n'
ENGLISH_WORDS = set(Path('dictionary.txt').read_text().splitlines())


def get_english_count(message):
    message = message.upper()
    message = remove_non_letters(message)
    possible_words = message.split()

    if possible_words == []:
        return 0.0

    matches = sum(word in ENGLISH_WORDS for word in possible_words)
    return matches / len(possible_words)


def remove_non_letters(message):
    return ''.join(symbol for symbol in message
                   if symbol in LETTERS_AND_SPACE)


def is_english(message, word_percentage=20, letter_percentage=85):
    words_match = get_english_count(message) * 100 >= word_percentage
    num_letters = len(remove_non_letters(message))
    message_letters_percentage = num_letters / len(message) * 100
    letters_match = message_letters_percentage >= letter_percentage
    return words_match and letters_match
