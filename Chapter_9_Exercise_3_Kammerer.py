def encrypt_text(text):

    encrypt_codes = {'H': '!', 'e': '$', 'l': '|', 'o': 'B', 'W': '^', 'r': '&', 'd': '*', ',': 'U', ' ': 'R'}

    encrypted_text = ""
    for letter in text:
        encrypted_text = encrypted_text + encrypt_codes[letter]

    return encrypted_text


def decrypt_text(encrypted_text):

    decrypt_codes = {'!': 'H', '$': 'e', '|': 'l', 'B': 'o', '^': 'W', '&': 'r', '*': 'd', 'U': ',', 'R': " "}

    decrypted_text = ""
    for letter in encrypted_text:
        decrypted_text = decrypted_text + decrypt_codes[letter]

    return decrypted_text


def main():

    text = "Hello, World"

    encrypted_text = encrypt_text(text)
    decrypted_text = decrypt_text(encrypted_text)

    print(encrypted_text)
    print(decrypted_text)


main()
