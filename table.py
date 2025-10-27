import math
import re

KEY = "SECRET"


def get_transposition_order(key):
    indexed_key = list(enumerate(key))
    sorted_key = sorted(indexed_key, key=lambda x: (x[1], x[0]))
    return [index for index, letter in sorted_key]


def normalize_text(text):
    return re.sub(r"[^A-Z]", "", text.upper())


def transposition_encrypt(plaintext, key=KEY):
    text = normalize_text(plaintext)
    key_length = len(key)
    order = get_transposition_order(key)

    if not text:
        return ""

    num_rows = math.ceil(len(text) / key_length)

    grid = [["" for _ in range(key_length)] for _ in range(num_rows)]

    text_index = 0
    for r in range(num_rows):
        for c in range(key_length):
            if text_index < len(text):
                grid[r][c] = text[text_index]
                text_index += 1

    ciphertext = []

    for col_index_to_read in order:
        for r in range(num_rows):
            char = grid[r][col_index_to_read]
            if char:
                ciphertext.append(char)

    return "".join(ciphertext)


def transposition_decrypt(ciphertext, key=KEY):
    key_length = len(key)
    order = get_transposition_order(key)
    cipher_length = len(ciphertext)

    if not ciphertext:
        return ""

    num_rows = math.ceil(cipher_length / key_length)
    num_nulls = (key_length * num_rows) - cipher_length
    num_full_cols_in_last_row = key_length - num_nulls

    grid = [["" for _ in range(key_length)] for _ in range(num_rows)]
    col_lengths = {}

    for c in range(key_length):
        if c < num_full_cols_in_last_row:
            col_lengths[c] = num_rows
        else:
            col_lengths[c] = num_rows - 1

    cipher_index = 0

    for col_original_index in order:
        current_col_length = col_lengths[col_original_index]
        for r in range(current_col_length):
            if cipher_index < cipher_length:
                grid[r][col_original_index] = ciphertext[cipher_index]
                cipher_index += 1

    plaintext = []
    for r in range(num_rows):
        for c in range(key_length):
            char = grid[r][c]
            if char:
                plaintext.append(char)

    return "".join(plaintext)


if __name__ == "__main__":
    source_filename = "source.txt"
    with open(source_filename, "r", encoding="UTF-8") as f:
        plaintext = f.read()

    normalized_original_text = normalize_text(plaintext)
    print(f"Вихідний текст: {normalized_original_text}")
    encrypted_text = transposition_encrypt(plaintext, KEY)

    print(f"Зашифрований текст: {encrypted_text}")

    text_to_decrypt = encrypted_text
    decrypted_text = transposition_decrypt(text_to_decrypt, KEY)
    print(f"Розшифрований текст: {decrypted_text}")

    if decrypted_text == normalized_original_text:
        print("\n✅ Успіх! Дешифрований текст повністю збігається з оригіналом.")
    else:
        print("\n❌ Помилка! Дешифрований текст не збігається з оригіналом.")
        print(f"Дешифрований (перші 50): {decrypted_text[:50]}")
        print(f"Оригінал (перші 50):     {normalized_original_text[:50]}")
        for i in range(min(len(decrypted_text), len(normalized_original_text))):
            if decrypted_text[i] != normalized_original_text[i]:
                print(
                    f"Різниця на позиції {i}: Дешифрований='{decrypted_text[i]}', Оригінал='{normalized_original_text[i]}'"
                )
                break
