from encrypt import *
from decrypt import *

# Driver function
plane_text1 = input("Enter plane text: ").upper()  
key1 = int(input("Enter Key: ")) 
cipher_text1 = encrypt(plane_text1, key1)
print("Cipher text: " + cipher_text1)

print("\n----------------------------------------------------\n")

cipher_text2 = input("Enter cipher text: ").upper() 
key2 = int(input("Enter Key: "))
plane_text2 = decrypt(cipher_text2, key2)
print("Plane text: " + plane_text2)