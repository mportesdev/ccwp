def encrypt_message(key, message):
    cipher_columns = [message[column::key] for column in range(key)]

    return ''.join(cipher_columns)
