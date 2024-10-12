# Функция для преобразования текста в двоичное представление (поддержка UTF-8)
function text_to_binary(text::String)
    return join([string(Int(c), base=2, pad=32) for c in text])  # Увеличьте заполнение до 32 для UTF-8
end

# Функция для преобразования двоичного кода в текст (поддержка UTF-8)
function binary_to_text(bin::String)
    chars = [parse(UInt32, b, base=2) for b in Iterators.partition(bin, 32)]  # Используйте UInt32 для UTF-8
    return String(Char.(chars))
end

# Функция шифрования XOR
function xor_encrypt(plaintext::String, key::String)
    # Преобразование текста и ключа в двоичный код
    binary_plaintext = text_to_binary(plaintext)
    binary_key = text_to_binary(key)
    
    # Убедитесь, что ключ не короче текста
    if length(binary_key) < length(binary_plaintext)
        error("Ключ должен быть не короче текста.")
    end
    
    # Применение XOR к битам текста и ключа
    encrypted_bits = [parse(Int, binary_plaintext[i]) ⊻ parse(Int, binary_key[i]) for i in 1:length(binary_plaintext)]
    
    # Объединение результата и преобразование обратно в строку
    encrypted_binary = join(encrypted_bits)
    return binary_to_text(encrypted_binary)
end

# Функция расшифровки XOR (аналогична шифрованию)
function xor_decrypt(ciphertext::String, key::String)
    return xor_encrypt(ciphertext, key)  # Расшифровка XOR такая же, как и шифрование
end

# Функция линейного конгруэнтного генератора (LCG)
function lcg(a, b, m, seed, length)
    random_sequence = Int[]
    yi = seed
    for i in 1:length
        yi = (a * yi + b) % m
        push!(random_sequence, yi)
    end
    return random_sequence
end

# Меню для выбора операций
function menu()
    println("Выберите операцию:")
    println("1. Зашифровать текст с помощью XOR")
    println("2. Расшифровать текст с помощью XOR")
    println("3. Сгенерировать ключ с помощью линейного конгруэнтного генератора (LCG)")
    println("4. Выйти")
    return parse(Int, readline())
end

# Основная программа
function main()
    while true
        choice = menu()

        if choice == 1
            println("Введите текст для шифрования:")
            plaintext = readline()
            println("Введите ключ (должен быть не короче текста):")
            key = readline()
            encrypted_text = xor_encrypt(plaintext, key)
            println("Зашифрованный текст: ", encrypted_text)

        elseif choice == 2
            println("Введите зашифрованный текст:")
            ciphertext = readline()
            println("Введите ключ для расшифровки:")
            key = readline()
            decrypted_text = xor_decrypt(ciphertext, key)
            println("Расшифрованный текст: ", decrypted_text)

        elseif choice == 3
            println("Введите параметры LCG:")
            println("Введите значение для a:")
            a = parse(Int, readline())
            println("Введите значение для b:")
            b = parse(Int, readline())
            println("Введите значение для m:")
            m = parse(Int, readline())
            println("Введите начальное значение (seed):")
            seed = parse(Int, readline())
            println("Введите длину ключа:")
            length = parse(Int, readline())
            random_sequence = lcg(a, b, m, seed, length)
            println("Сгенерированная последовательность ключей: ", random_sequence)

        elseif choice == 4
            println("Выход...")
            break

        else
            println("Неверная опция. Попробуйте еще раз.")
        end
    end
end

# Запуск основной программы
main()
