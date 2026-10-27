# Experiment 8: Keyword-Based Monoalphabetic Substitution
# Aim: Generate a cipher alphabet from a keyword and encrypt plaintext.
# Example keyword: CIPHER

import string

ALPHABET = string.ascii_uppercase

def keyword_alphabet(keyword):
    sequence = ""
    for ch in (keyword + ALPHABET).upper():
        if ch.isalpha() and ch not in sequence:
            sequence += ch
    return sequence

def encrypt(text, cipher_alphabet):
    result = ""
    for ch in text:
        if ch.isupper():
            result += cipher_alphabet[ord(ch) - ord("A")]
        elif ch.islower():
            result += cipher_alphabet[ord(ch.upper()) - ord("A")].lower()
        else:
            result += ch
    return result

def main():
    keyword = input("Enter keyword: ")
    cipher_alphabet = keyword_alphabet(keyword)
    print("Plain alphabet :", ALPHABET)
    print("Cipher alphabet:", cipher_alphabet)
    text = input("Enter plaintext: ")
    print("Ciphertext:", encrypt(text, cipher_alphabet))

if __name__ == "__main__":
    main()
