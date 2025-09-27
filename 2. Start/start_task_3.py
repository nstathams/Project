morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----'
}
def textmorse(text):
    morse_code = []
    for caps in text.upper():
        if caps in morse_dict:
            morse_code.append(morse_dict[caps])
        else:
            morse_code.append('/')
    return ' '.join(morse_code)
word = input("Введите слово: ")
morseout = textmorse(word)
print(f"Код морзе для слова '{word}': {morseout}")
