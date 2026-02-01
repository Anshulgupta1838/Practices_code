def encrypt_rail_fence(text, key):
    # Create empty rails
    rails = ['' for _ in range(key)]
    row = 0
    direction = 1  # 1 = down, -1 = up

    text = text.replace(" ", "")  # remove spaces

    for char in text:
        rails[row] += char
        row += direction

        # Reverse direction at top or bottom
        if row == 0 or row == key - 1:
            direction *= -1

    # Combine rows to form ciphertext
    return ''.join(rails)


def decrypt_rail_fence(cipher, key):
    # Step 1: Mark the zigzag pattern
    mark = [['' for _ in range(len(cipher))] for _ in range(key)]
    row, direction = 0, 1

    for i in range(len(cipher)):
        mark[row][i] = '*'
        row += direction

        if row == 0 or row == key - 1:
            direction *= -1

    # Step 2: Fill the marked spots with cipher characters
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if mark[i][j] == '*':
                mark[i][j] = cipher[index]
                index += 1

    # Step 3: Read zigzag to get plaintext
    result = ''
    row, direction = 0, 1

    for i in range(len(cipher)):
        result += mark[row][i]
        row += direction

        if row == 0 or row == key - 1:
            direction *= -1

    return result

plaintext = input("Enter Plaintext: ")
key = int(input("Enter Key (Number of Rails): "))

cipher = encrypt_rail_fence(plaintext, key)
print("\nEncrypted Text:", cipher)

decrypted = decrypt_rail_fence(cipher, key)
print("Decrypted Text:", decrypted)