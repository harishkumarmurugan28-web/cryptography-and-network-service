# Experiment 2: Monoalphabetic Substitution Cipher
# Aim: Replace each plaintext letter using a unique 26-letter ciphertext alphabet.

import string

ALPHABET = string.ascii_uppercase

def encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isupper():
            result += key[ord(ch) - ord("A")]
        elif ch.islower():
            result += key[ord(ch.upper()) - ord("A")].lower()
        else:
            result += ch
    return result

def main():
    key = input("Enter 26-letter substitution key: ").upper()
    if len(key) != 26 or not key.isalpha() or len(set(key)) != 26:
        print("Invalid key! Use all 26 letters exactly once.")
        return
    text = input("Enter plaintext: ")
    print("Ciphertext:", encrypt(text, key))

if __name__ == "__main__":
    main()
