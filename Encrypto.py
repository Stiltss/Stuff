import os
from cryptography.fernet import Fernet
import time
import base64
import sys  # All the imports


# Phrase to Encrypt
pte = input("Phrase To Encrypt: ")
bkey = Fernet.generate_key()
key = bkey.decode('utf-8')

print("Key to Decrypt(DO NOT SHARE UNLESS YOU WANT TEXT TO BE DECRYPTED): " + key)
time.sleep(3)

# Recoding the b-key
bkey = key.encode('utf-8')

f = Fernet(bkey)
token = f.encrypt(pte.encode('utf-8'))
print("")
print("Encrypted Phrase: " + token.decode('utf-8'))  # Decode the token for cleaner output
time.sleep(1)
print("10 seconds before clearing text")
time.sleep(10)
os.system("clear")

decrypt = input("Do you wish to decrypt something?(Y/N): ").strip()
while decrypt.upper() not in ['Y', 'N']:
    print("Invalid Input. Y or N")
    time.sleep(0.5)
    decrypt = input("Do you wish to decrypt something?(Y/N): ").strip()

if decrypt.upper() == "Y":
    Dkey = input("Key to Decrypt the text: ")
    dp = input("Phrase to decrypt: ")
    dkey = Dkey.encode('utf-8')
    DP = dp.encode('utf-8')
    ff = Fernet(dkey)
    resp = ff.decrypt(DP).decode('utf-8')
    
    for i in range(10):       
        print("     Decrypting. Please Hold")
        print(f"[{'█' * (i+1)}{'-' * (9-i)}]")
        time.sleep(0.5)
        os.system("clear")
    print("Decrypted Text: " + resp)
    
sys.exit(0)  # End the code
