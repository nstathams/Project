def _encrypt(text, shift):
    r = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift_ = (ord(char) - base + shift) % 26
            r += chr(base + shift_)
        else:
            r += char
    return r

def _decrypt(text, shift):
    return _encrypt(text, -shift)

if __name__ == "__main__":
    x = input("Введите текст: ")
    key = int(input("Введите ключ (число от 0 до 25): "))

    encrypted = _encrypt(x, key)
    print(f"Зашифрованный текст: {encrypted}")

    decrypted = _decrypt(encrypted, key)
    print(f"Дешифрованный текст: {decrypted}")
