"""Напишите функцию count_morse_characters(), которая принимает строку, состоящую из символов азбуки Морзе,
и возвращает количество символов (точек и/или тире) в ней."""


def count_morse_characters(text):
    count_char = 0
    for char in text:
        if char == " ":
            continue
        else:
            count_char += 1
    return count_char


text_morse = ".--- .- ...- .-"

print(count_morse_characters(text_morse))
