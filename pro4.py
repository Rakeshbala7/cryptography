import string
def encrypt(plaintext, key):
    ciphertext = ""
    key_idx = 0
    for char in plaintext:
        if char.isalpha():
            key_char = key[key_idx % len(key)]
            key_idx += 1
            shift = string.ascii_lowercase.index(key_char.lower())
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += char
    return ciphertext
plaintext = "The quick brown fox jumps over the lazy dog."
key = "secret"
ciphertext = encrypt(plaintext, key)
print("Plaintext: ", plaintext)
print("Ciphertext:", ciphertext)