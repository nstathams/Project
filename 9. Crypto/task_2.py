def rot13(text: str) -> str:
    r = "" 
    for char in text:
        if char.isalpha():
            if char.isupper():
                shifted = (ord(char) - ord('A') + 13) % 26
                r += chr(ord('A') + shifted)
            else:
                shifted = (ord(char) - ord('a') + 13) % 26
                r += chr(ord('a') + shifted)
        else:
            r += char
    return r
print('\n-----------------------\n')
print(rot13("Hello, World!"))        # Должно вернуть: "Uryyb, Jbeyq!"
print(rot13("Uryyb, Jbeyq!"))        # Должно вернуть: "Hello, World!"
print(rot13(rot13("Test")))          # Должно вернуть: "Test"
print(rot13("123!@#"))               # Должно вернуть: "123!@#" (без изменений)

print('\n-----------------------\n')

def caesar_(text: str, shift: int, mode: str = 'encrypt') -> str:

    result = ""
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                shifted = (ord(char) - ord('A') + shift) % 26
                result += chr(ord('A') + shifted)
            else:
                shifted = (ord(char) - ord('a') + shift) % 26
                result += chr(ord('a') + shifted)
        else:
            result += char
    
    return result

print(caesar_("Hello", 3, 'encrypt'))           # Khoor
print(caesar_("Khoor", 3, 'decrypt'))           # Hello
print(caesar_("XYZ", 5, 'encrypt'))             # CDE (циклический сдвиг)
print(caesar_("Hello, World!", 13, 'encrypt'))  # Uryyb, Jbeyq!

