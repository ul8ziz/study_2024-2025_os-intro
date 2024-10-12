# Function to convert text to its binary representation (UTF-8 support)
function text_to_binary(text::String)
    return join([string(Int(c), base=2, pad=32) for c in text])  # Increase padding to 32 for UTF-8
end

# Function to convert binary to text (UTF-8 support)
function binary_to_text(bin::String)
    chars = [parse(UInt32, b, base=2) for b in Iterators.partition(bin, 32)]  # Use UInt32 for UTF-8
    return String(Char.(chars))
end

# XOR encryption function
function xor_encrypt(plaintext::String, key::String)
    # Convert text and key to binary
    binary_plaintext = text_to_binary(plaintext)
    binary_key = text_to_binary(key)
    
    # Ensure the key is at least as long as the plaintext
    if length(binary_key) < length(binary_plaintext)
        error("Key should be as long as or longer than the plaintext.")
    end
    
    # XOR the bits of the plaintext and the key
    encrypted_bits = [parse(Int, binary_plaintext[i]) ⊻ parse(Int, binary_key[i]) for i in 1:length(binary_plaintext)]
    
    # Join the result and convert it back to a string
    encrypted_binary = join(encrypted_bits)
    return binary_to_text(encrypted_binary)
end

# XOR decryption function (same as encryption for XOR)
function xor_decrypt(ciphertext::String, key::String)
    return xor_encrypt(ciphertext, key)  # XOR decryption is the same as encryption
end

# Linear Congruential Generator (LCG) function
function lcg(a, b, m, seed, length)
    random_sequence = Int[]
    yi = seed
    for i in 1:length
        yi = (a * yi + b) % m
        push!(random_sequence, yi)
    end
    return random_sequence
end

# Menu for choosing operations
function menu()
    println("Choose an operation:")
    println("1. Encrypt text using XOR")
    println("2. Decrypt text using XOR")
    println("3. Generate key using Linear Congruential Generator (LCG)")
    println("4. Exit")
    return parse(Int, readline())
end

# Main program
function main()
    while true
        choice = menu()

        if choice == 1
            println("Enter the plaintext to encrypt:")
            plaintext = readline()
            println("Enter the key (should be as long as or longer than the text):")
            key = readline()
            encrypted_text = xor_encrypt(plaintext, key)
            println("Encrypted text: ", encrypted_text)

        elseif choice == 2
            println("Enter the encrypted text:")
            ciphertext = readline()
            println("Enter the key used for decryption:")
            key = readline()
            decrypted_text = xor_decrypt(ciphertext, key)
            println("Decrypted text: ", decrypted_text)

        elseif choice == 3
            println("Enter LCG parameters:")
            println("Enter value for a:")
            a = parse(Int, readline())
            println("Enter value for b:")
            b = parse(Int, readline())
            println("Enter value for m:")
            m = parse(Int, readline())
            println("Enter the seed (initial value):")
            seed = parse(Int, readline())
            println("Enter the length of the key:")
            length = parse(Int, readline())
            random_sequence = lcg(a, b, m, seed, length)
            println("Generated key sequence: ", random_sequence)

        elseif choice == 4
            println("Exiting...")
            break

        else
            println("Invalid option. Please try again.")
        end
    end
end

# Run the main program
main()
