# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',  'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--', 'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-','R': '.-.', 'S': '...',  'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--','Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.',  ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'  # Space between words
}

# Reverse Dictionary
MORSE_TO_TEXT_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def morse_to_text(morse):
    words = morse.strip().split(' / ')  # Morse words are separated by '/'
    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_letters = [MORSE_TO_TEXT_DICT.get(symbol, '?') for symbol in letters]
        decoded_words.append(''.join(decoded_letters))
    return ' '.join(decoded_words)

def text_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('?')  # Unknown character
    return ' '.join(morse_code)
