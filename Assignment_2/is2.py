def encrypt_transposition(text, key):
    # Generate the order of columns based on the key
    order = {char: i + 1 for i, char in enumerate(sorted(key))}

    # Calculate the number of rows needed in the table
    num_rows = len(text) // len(key)
    if len(text) % len(key) != 0:
        num_rows += 1

    # Create the table
    table = [[' ' for _ in range(len(key))] for _ in range(num_rows)]

    # Fill in the table with the characters from the text
    index = 0
    for row in range(num_rows):
        for col in range(len(key)):
            if index < len(text):
                table[row][col] = text[index]
                index += 1
            else:
                break

    # Create the encrypted text based on the column order
    encrypted_text = ''
    for col in sorted(order, key=lambda x: order[x]):
        for row in range(num_rows):
            char = table[row][key.index(col)]
            encrypted_text += char if char != ' ' else '*'

    return encrypted_text


text = "Tejas Labde"
key = "HACK"
encrypted_text = encrypt_transposition(text, key)
print("Encrypted Text:", encrypted_text)

def decrypt_transposition(encrypted_text, key):
    # Generate the order of columns based on the key
    order = {char: i + 1 for i, char in enumerate(sorted(key))}

    # Calculate the number of rows needed in the table
    num_rows = len(encrypted_text) // len(key)

    # Create the table
    table = [[' ' for _ in range(len(key))] for _ in range(num_rows)]

    # Fill in the table with the characters from the encrypted text
    index = 0
    for col in sorted(order, key=lambda x: order[x]):
        for row in range(num_rows):
            table[row][key.index(col)] = encrypted_text[index]
            index += 1

    # Create the decrypted text
    decrypted_text = ''
    for row in range(num_rows):
        for col in range(len(key)):
            decrypted_text += table[row][col]

    # Replace '*' with space
    decrypted_text = decrypted_text.replace('*', ' ')

    return decrypted_text

decrypted_text = decrypt_transposition(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
