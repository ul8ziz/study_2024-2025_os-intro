# Лабораторная работа №1

k = 3

def caesar_cipher(text, k):
    result = ""
    for char in text:
        match char: 
            case char if 'А' <= char <= 'Я':
                new_char = chr((ord(char) - ord('А') + k) % 32 + ord('А'))
            case char if 'а' <= char <= 'я':
                new_char = chr((ord(char) - ord('а') + k) % 32 + ord('а'))
            case char if 'A' <= char <= 'Z':
                new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            case char if 'a' <= char <= 'z':
                new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            case _:
                new_char = char
        result += new_char
    return result

def atbash_cipher(text):
    result = ""
    for char in text:
        match char: 
            case char if 'А' <= char <= 'Я':
                new_char = chr(ord('А')+ (ord('Я') - ord(char)))
            case char if 'а' <= char <= 'я':
                new_char = chr(ord('а')+ (ord('я') - ord(char)))
            case char if 'A' <= char <= 'Z':
                new_char = chr(ord('A')+ (ord('Z') - ord(char)))
            case char if 'a' <= char <= 'z':
                new_char = chr(ord('a')+ (ord('z') - ord(char)))
            case _:
                new_char = char
        result += new_char
    return result

text = input("Введите текст:\t")
encrypted_caesar = caesar_cipher(text, k)
print("Шифр Цезаря:\t", encrypted_caesar)
encrypted_atbash = atbash_cipher(text)
print("Шифр Атбаш:\t", encrypted_atbash)