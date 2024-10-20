#!/usr/bin/python3 

morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'}

message = input("enter message to send as morse code: ").strip()

def encode(message):
    morse_code = ''
    for char in message.upper():
        if char in morse_dict:
            morse_code += morse_dict[char] + ' '
        else:
            print(f"{char} is invalid character.\n")
    return morse_code
print(f"Message: {message} \nMorse code sequence:  {encode(message)}")

def decode(morse_code_message):
    text_msg =''
    morse_code = morse_code_message.split(" ") 
    for word in morse_code:
        for char,morse in morse_dict.items():
            if morse == word: 
                text_msg += char
    return text_msg
morse_code_message= "-.... .--- / ..-.. -.-"
print(f"Morse code = {morse_code_message} \nDecoded to text={decode(morse_code_message)}")




