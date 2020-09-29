# Function for encryption
def shift_encrypt(plain_text, key):
    cipher = ""
    for ch in plain_text:
        cipher += chr(((ord(ch) + key - 65)%26)+65)
    return cipher
