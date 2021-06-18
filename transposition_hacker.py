from detect_english import is_english
from transposition import decrypt


def hack(message):
    for key in range(1, len(message)):
        decrypted_text = decrypt(message, key)

        if is_english(decrypted_text):
            return decrypted_text, key
