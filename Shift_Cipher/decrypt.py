# Function for decryption
def decrypt(cipher_text, key):
    plane = ""
    for ch in cipher_text:
        plane += chr(((ord(ch) - key - 65)%26)+65)
    return plane