KEY = "CRYPTOGRAPHY"


def vigenere_encrypt(text: str, key: str) -> str:
    result = []
    key_chars = [c.upper() for c in key if c.isalpha()]
    key_len = len(key_chars)

    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            text_num = ord(char) - base
            key_num = ord(key_chars[key_index % key_len]) - ord("A")
            new_num = (text_num + key_num) % 26
            result.append(chr(base + new_num))
            key_index += 1
        else:
            result.append(char)

    return "".join(result)


def vigenere_encrypt_short(text: str, key: str) -> str:
    result = []
    key_chars = [c.upper() for c in key if c.isalpha()]
    key_len = len(key_chars)

    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            text_num = ord(char) - base
            key_num = ord(key_chars[key_index % key_len]) - ord("A")
            new_num = (text_num + key_num) % 26
            result.append(chr(base + new_num))
            key_index += 1

    return "".join(result)


def vigenere_decrypt(cipher_text: str, key: str) -> str:
    result = []
    key_chars = [c.upper() for c in key if c.isalpha()]
    key_len = len(key_chars)

    key_index = 0

    for char in cipher_text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            cipher_num = ord(char) - base
            key_num = ord(key_chars[key_index % key_len]) - ord("A")
            new_num = (cipher_num - key_num + 26) % 26
            result.append(chr(base + new_num))
            key_index += 1
        else:
            result.append(char)

    return "".join(result)


def main():
    source_filename = "source.txt"
    with open(source_filename, "r", encoding="UTF-8") as f:
        text = f.read()

    if not text.strip():
        print("Помилка: Вхідний файл порожній.")
        return

    encrypted_text = vigenere_encrypt(text, KEY)
    encrypted_filename = "encrypted.txt"
    with open(encrypted_filename, "w", encoding="UTF-8") as f:
        f.write(encrypted_text)
    print(
        f"Зашифрований текст: {encrypted_text}..., збережено до файлу {encrypted_filename}"
    )

    encrypted_text_short = vigenere_encrypt_short(text, KEY)
    encrypted_filename_short = "encrypted_short.txt"
    with open(encrypted_filename_short, "w", encoding="UTF-8") as f:
        f.write(encrypted_text_short)
    print(
        f"Зашифрований текст: {encrypted_text_short}..., збережено до файлу {encrypted_filename_short}"
    )

    with open(encrypted_filename, "r", encoding="UTF-8") as f:
        text_to_decrypt = f.read()

    decrypted_text = vigenere_decrypt(text_to_decrypt, KEY)
    decrypted_filename = "decrypted.txt"
    with open(decrypted_filename, "w", encoding="UTF-8") as f:
        f.write(decrypted_text)
    print(
        f"Розшифрований текст: {decrypted_text}..., збережено до файлу {decrypted_filename}"
    )
    is_successful = text.strip() == decrypted_text.strip()
    print(
        f"Розшифрований текст ідентичний оригіналу: {'Так' if is_successful else 'Ні'}"
    )

    with open(encrypted_filename_short, "r", encoding="UTF-8") as f:
        text_to_decrypt = f.read()

    decrypted_text_short = vigenere_decrypt(text_to_decrypt, KEY)
    decrypted_filename_short = "decrypted_short.txt"
    with open(decrypted_filename_short, "w", encoding="UTF-8") as f:
        f.write(decrypted_text_short)
    print(
        f"Розшифрований текст: {decrypted_text_short}..., збережено до файлу {decrypted_filename_short}"
    )


if __name__ == "__main__":
    main()
