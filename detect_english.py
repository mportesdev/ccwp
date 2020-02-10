# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPER_LETTERS + UPPER_LETTERS.lower() + ' \t\n'


def load_dictionary():
    dictionary_file = open('dictionary.txt')
    english_words = {}
    for word in dictionary_file.read().split('\n'):
        english_words[word] = None
    dictionary_file.close()
    return english_words


ENGLISH_WORDS = load_dictionary()


def get_english_count(message):
    message = message.upper()
    message = remove_non_letters(message)
    possible_words = message.split()

    if possible_words == []:
        return 0.0

    matches = 0
    for word in possible_words:
        if word in ENGLISH_WORDS:
            matches += 1
    return matches / len(possible_words)


def remove_non_letters(message):
    letters_only = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            letters_only.append(symbol)
    return ''.join(letters_only)


def is_english(message, word_percentage=20, letter_percentage=85):
    words_match = get_english_count(message) * 100 >= word_percentage
    num_letters = len(remove_non_letters(message))
    message_letters_percentage = num_letters / len(message) * 100
    letters_match = message_letters_percentage >= letter_percentage
    return words_match and letters_match
