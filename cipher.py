# Caesar Cipher Implementation

def encrypt(text, key):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(cipher, key):
    result = ""
    for char in cipher:
        if char.isupper():
            result += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - key - 97) % 26 + 97)
        else:
            result += char
    return result

# Main program
plaintext = input("Enter plaintext: ")
key = int(input("Enter key (1-25): "))

ciphertext = encrypt(plaintext, key)
print("Encrypted Text:", ciphertext)

decrypted_text = decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)