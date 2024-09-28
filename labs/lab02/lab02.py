# Лабораторная работа №2
import math
import random
import numpy as np
from colorama import Fore, Style, init

init(autoreset=True)

russian_letters = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
russian_matrix = np.empty((len(russian_letters), len(russian_letters)), dtype='<U1')
for i in range(len(russian_letters)):
    for j in range(len(russian_letters)):
        letter_index = (i + j) % len(russian_letters)
        russian_matrix[i][j] = russian_letters[letter_index]

def rotate_matrix_clocwise(matrix):
    transposed_matrix = []
    for j in range(len(matrix[0]) - 1, -1, -1):
        new_row = []
        for i in range(len(matrix)):
            new_row.append(matrix[i][j])
        transposed_matrix.append(new_row)
    return transposed_matrix

def cryptogram(matrix, password):
    matrix.append([''] * len(password))
    matrix.append([''] * len(password))
    j = 0
    for char in password:
        matrix[-2][j] = char
        matrix[-1][j] = ord(char)
        j += 1

    for i in range(len(matrix[:-1])):
        for j in range(len(matrix[i])):
            value = matrix[i][j]
            if i == len(matrix[:-2]):
                print(Fore.GREEN + str(value) + Style.RESET_ALL, end=' ')
            else:
                print(value, end=' ')
        print()

    last_row = matrix[-1]
    sorted_indices = sorted(range(len(last_row)), key=lambda x: last_row[x])
    sorted_matrix = []
    for row in matrix[:-2]:
        sorted_row = [row[i] for i in sorted_indices]
        sorted_matrix.append(sorted_row)
    transposed_matrix = [[row[i] for row in sorted_matrix] for i in range(len(sorted_matrix[0]))]
    result = ''.join(''.join(row) for row in transposed_matrix)
    return result

def route_cipher(text, password):
    rows = math.ceil(len(text)/len(password))
    cols = len(password)
    matrix = []
    for _ in range(rows):
        row = [random.choice(russian_letters) for _ in range(cols)]
        matrix.append(row)

    i, j = 0, 0
    for char in text:
        matrix[i][j] = char
        j += 1
        if j >= cols:
            i += 1
            j = 0

    print('Маршрутное шифрование:')
    return cryptogram(matrix, password)

def lattice_cipher(text, password):
    rows, cols = len(password), len(password)
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    k = int(len(password)/2)

    for _ in range(4):
        i, j, number = 0, 0, 0
        for i in range(k):
            for j in range(k):
                number += 1
                matrix[i][j] = number
            matrix = rotate_matrix_clocwise(matrix)

    unique_values = set()
    for row in matrix:
        unique_values.update(row)
    coordinates = {value: [] for value in unique_values}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            value = matrix[i][j]
            if value in coordinates:
                coordinates[value].append((i, j))
    selected_coordinates = {}
    for number in range(1, k**2+1):
        if coordinates[number]:
            selected_coordinates[number] = random.choice(coordinates[number])

    print("Решето:")
    for i in range(len(matrix)):
        for j in range (len(matrix[i])):
            value = matrix[i][j]
            if (i, j) in selected_coordinates.values():
                print(Fore.RED + str(value) + Style.RESET_ALL, end=' ')
            else:
                print(value, end=' ')
        print()
    
    letter, i, j, count = 0, 0, 0, 0
    while count < k**2:
        if (i, j) in selected_coordinates.values():
            matrix[i][j] = text[letter]
            letter += 1
            count += 1
        j += 1
        if j >= cols:
            i += 1
            j = 0
    matrix = rotate_matrix_clocwise(matrix)

    i, j, count = rows - 1, 0, 0
    while count < k**2:
        if (i, j) in selected_coordinates.values():
            matrix[i][j] = text[letter]
            letter += 1
            count += 1
        i -= 1
        if i < 0:
            j += 1
            i = rows - 1
    matrix = rotate_matrix_clocwise(matrix)

    i, j, count = rows - 1, cols - 1, 0
    while count < k**2:
        if (i, j) in selected_coordinates.values():
            matrix[i][j] = text[letter]
            letter += 1
            count += 1
        j -= 1
        if j < 0:
            i -= 1
            j = cols - 1
    matrix = rotate_matrix_clocwise(matrix)

    i, j, count = 0, cols - 1, 0
    while count < k**2:
        if (i, j) in selected_coordinates.values():
            matrix[i][j] = text[letter]
            letter += 1
            count += 1
        i += 1
        if i >= rows:
            j -= 1
            i = 0
    matrix = rotate_matrix_clocwise(matrix)

    print('Шифрование с помощью решёток:')
    return cryptogram(matrix, password)

def vigener_cipher(text, password):
    row1 = list(text)
    repeated_password = (password * (len(text) // len(password) + 1))[:len(text)]
    row2 = list(repeated_password)
    row3 = ['' for _ in range(len(text))]
    matrix = [row1, row2, row3]

    n, index_i, index_j = 0, -1, -1
    for n in range(len(text)):
        for j in range(len(russian_matrix[0])):
            if russian_matrix[0][j] == matrix [0][n]:
                index_j = j
                break
        for i in range(len(russian_matrix)):
            if russian_matrix[i][0] == matrix [1][n]:
                index_i = i
                break
        matrix[2][n] = russian_matrix[index_i][index_j]

    print("Шифр Виженера:")
    for i in range(len(matrix)):
        for j in range (len(matrix[i])):
            value = matrix[i][j]
            if i == len(matrix[:-1]):
                print(Fore.GREEN + str(value) + Style.RESET_ALL, end=' ')
            else:
                print(value, end=' ')
        print()
    return

print('Выберите один из шифров перестановки:')
print('1. Маршрутное шифрование')
print('2. Шифрование с помощью решёток')
print("3. Таблица Виженера")
choice = input('Введите номер выбранного шифра: ')
match choice:
    case '1':
        text = input('Введите текст: ')
        filter_text = ''.join(filter(str.isalnum, text)).upper()
        password = input('Введите пароль: ')
        filter_password = ''.join(filter(str.isalnum, password)).upper()
        if len(filter_text) > len(filter_password):
            if len(set(filter_password)) == len(filter_password):
                encrypted_route = route_cipher(filter_text, filter_password)
                print("Криптограмма:", encrypted_route)
            else:
                print('Буквы пароля не должны повторяться!')
        else:
            print('Текст должен быть длиннее пароля!')
    case '2':
        text = input('Введите текст: ')
        filter_text = ''.join(filter(str.isalnum, text)).upper()
        sqrt_text = math.ceil(math.sqrt(len(filter_text)))
        if sqrt_text % 2 == 1:
            sqrt_text += 1
        while len(filter_text) < (sqrt_text**2):
            filter_text += random.choice(russian_letters)
        password = input(f'Введите пароль длинной {sqrt_text} букв(ы): ')
        filter_password = ''.join(filter(str.isalnum, password)).upper()
        if len(set(filter_password)) == len(filter_password):
            if sqrt_text == len(filter_password):
                encrypted_lattice = lattice_cipher(filter_text, filter_password)
                print("Криптограмма:", encrypted_lattice)
            else:
                print(f'В пароле должно быть {sqrt_text} букв(ы)!')
        else:
            print('Буквы пароля не должны повторяться!')
    case '3':
        text = input('Введите текст: ')
        filter_text = ''.join(filter(str.isalnum, text)).upper()
        password = input('Введите пароль: ')
        filter_password = ''.join(filter(str.isalnum, password)).upper()
        if len(filter_text) > len(filter_password):
            if all('А' <= char <= 'Я' for char in filter_text):
                if all('А' <= char <= 'Я' for char in filter_password):
                    vigener_cipher(filter_text, filter_password)
                else:
                    print('Пароль должен быть только из русских букв (и без ё)!')
            else:
                print('Текст должен быть только из русских букв (и без ё)!')
        else:
            print('Текст должен быть длиннее пароля!')
    case _:
        print('Некорректный выбор!')

# Добавляем строку для остановки программы
input("Нажмите Enter, чтобы завершить программу...")
