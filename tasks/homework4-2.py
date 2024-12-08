'''Вам предоставлен список английских слов и словарь соответствия символов строки коду азбуки Морзе.
Создайте функцию morse_encode(), которая принимает словарь с азбукой Морзе и слово для кодирования и возвращает его представление в азбуке Морзе с использованием пробелов между символами.'''

morse = {"0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
             "7": "--...", "8": "---..", "9": "----.", "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
             "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--",
             "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
             "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--",
             "?": "..--..", "!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.", ")": "-.--.-"}

words_to_decode = ['java', 'python', 'ruby', 'php', 'fortran', 'javascript', 'kotlin', 'swift', 'basic', 'pascal']


def morse_encode(morse, word = None):
    decoded_word = ""
    for char in word:
        if char in morse:
            decoded_word += morse[char] + " "
        else:
            decoded_word += char

    return decoded_word

print(morse_encode(morse, word = 'java'))

"""как ещё можно добавить пробел к получаемому значению из словаря без генераторных выражений"""
"""Вариант через метод .join()

def morse_encode(morse, word=None):
    encoded_chars = []
    for char in word:
        if char in morse:
            encoded_chars.append(morse[char])
        else:
            encoded_chars.append(char)
    print(encoded_chars)
    return ' '.join(encoded_chars)

print(morse_encode(morse, word='java'))"""

"""список words_to_decode дан по условию, но он тут не нужен, никак не используется для решения"""