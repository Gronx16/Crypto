# Generating plane text
def vingere_decrypt (cipher, str_key):
    plane = ""
    for i in range(len(cipher)):
        temp1 = ord(cipher[i]) - ord(str_key[i])
        plane += chr((temp1%26) + 65)
    return plane