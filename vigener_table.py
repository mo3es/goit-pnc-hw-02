import re

KEY = "MATRIX"
ALPHABET_SIZE = 26
A_ASCII = ord("A")


def prepare_key(text_length, key=KEY):
    normalized_key = re.sub(r"[^A-Z]", "", key.upper())
    repeated_key = (normalized_key * (text_length // len(normalized_key) + 1))[
        :text_length
    ]
    return repeated_key


def vigenere_table_encrypt(plaintext, key=KEY):
    ciphertext = []
    key_index = 0
    text_to_process = plaintext.upper()

    normalized_key = re.sub(r"[^A-Z]", "", key.upper())
    key_length = len(normalized_key)

    if key_length == 0:
        return plaintext

    for char in text_to_process:
        if "A" <= char <= "Z":
            p_val = ord(char) - A_ASCII
            k_val = ord(normalized_key[key_index % key_length]) - A_ASCII
            c_val = (p_val + k_val) % ALPHABET_SIZE
            ciphertext.append(chr(c_val + A_ASCII))
            key_index += 1
        else:
            ciphertext.append(char)
    return "".join(ciphertext)


def vigenere_table_decrypt(ciphertext, key=KEY):
    plaintext = []
    key_index = 0
    text_to_process = ciphertext.upper()
    normalized_key = re.sub(r"[^A-Z]", "", key.upper())
    key_length = len(normalized_key)

    if key_length == 0:
        return ciphertext

    for char in text_to_process:
        if "A" <= char <= "Z":
            c_val = ord(char) - A_ASCII
            k_val = ord(normalized_key[key_index % key_length]) - A_ASCII
            p_val = (c_val - k_val) % ALPHABET_SIZE
            plaintext.append(chr(p_val + A_ASCII))
            key_index += 1
        else:
            plaintext.append(char)
    return "".join(plaintext)


if __name__ == "__main__":
    source_filename = "source.txt"
    with open(source_filename, "r", encoding="UTF-8") as f:
        plaintext = f.read()

    print(f"Оригінальний текст: {plaintext}")

    encrypted_text = vigenere_table_encrypt(plaintext, KEY)
    print(f"Зашифрований текст: {encrypted_text}")

    decrypted_text = vigenere_table_decrypt(encrypted_text, KEY)
    print(f"Дешифрований текст: {decrypted_text}")
