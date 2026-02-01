def caesar_cipher_custom(text):
    result = ""

    for i, char in enumerate(text):
        if char.isalpha():
            # Odd index (1-based) → +3 shift
            if (i + 1) % 2 != 0:
                shift = 3
            else:  # Even index → -3 shift
                shift = -3

            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result
plain_text = "HELLO"
encrypted = caesar_cipher_custom(plain_text)
print("Encrypted:", encrypted)
