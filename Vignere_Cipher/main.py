from encrypt import *
from decrypt import *
from key_generator import *


# Taking input from the user for encryption
plain_text  = input("Enter the plain text: ").upper()
key_ = input("Enter key: ").upper()

key = keygen(plain_text, key_)
cipher_text = vigenere_encrypt(plain_text, key)
print("Cipher text: " + cipher_text)

print("\n------------------------------------------------\n")

# Taking input from the user for deccryption
cipher_text1  = input("Enter the cipher text: ").upper()
key1_ = input("Enter key: ").upper()

key1 = keygen(cipher_text1, key1_)
plain_text1 = vigenere_decrypt(cipher_text1, key1)
print("Plane text: " + plain_text1)