# Generating cipher text
def vingere_encrypt(plain_text, str_key):
    cipher = ""
    for i in range(len(plain_text)):
        temp = ord(plain_text[i]) + ord(str_key[i]) - 2*65
        cipher += chr((temp%26) + 65)
    return cipher