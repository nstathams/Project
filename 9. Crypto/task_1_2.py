def _bruteforce(ciphertext):
    for shift in range(26):
        r = ""
        for char in ciphertext:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base - shift) % 26
                r += chr(base + shifted)
            else:
                r += char
        print(f"Ключ {shift}: {r}")

if __name__ == "__main__":
    encrypted_ = input("Введите зашифрованный текст: ")
    _bruteforce(encrypted_)
