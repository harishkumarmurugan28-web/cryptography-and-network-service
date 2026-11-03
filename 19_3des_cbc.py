# Requires: python3 -m pip install pycryptodome
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad
key=DES3.adjust_key_parity(get_random_bytes(24));iv=get_random_bytes(8)
p=input("Plaintext: ").encode()
c=DES3.new(key,DES3.MODE_CBC,iv).encrypt(pad(p,8))
print("Key:",key.hex());print("IV:",iv.hex());print("Ciphertext:",c.hex())
print("Decrypted:",unpad(DES3.new(key,DES3.MODE_CBC,iv).decrypt(c),8).decode())
print("3DES is legacy; use AES-GCM for new systems. Security: modern authenticated encryption; performance: AES is usually faster.")
