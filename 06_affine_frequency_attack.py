# Experiment 6: Affine Cipher Frequency Attack
# Assumption: most frequent ciphertext letter B represents plaintext E,
# and second most frequent U represents plaintext T.
# This gives a=3, b=15 for C=(a*p+b) mod 26. The inverse of 3 mod 26 is 9.

from math import gcd

def mod_inverse(a, m=26):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def decrypt(text, a, b):
    inv = mod_inverse(a)
    if inv is None:
        raise ValueError("a has no modular inverse modulo 26.")
    result = ""
    for ch in text:
        if ch.isupper():
            c = ord(ch) - ord("A")
            result += chr(((inv * (c - b)) % 26) + ord("A"))
        elif ch.islower():
            c = ord(ch) - ord("a")
            result += chr(((inv * (c - b)) % 26) + ord("a"))
        else:
            result += ch
    return result

def main():
    # B -> E and U -> T are frequency-analysis assumptions.
    a, b = 3, 15
    print("Assuming B -> E and U -> T:")
    print("Affine encryption key: a =", a, ", b =", b)
    print("Decryption formula: p = 9(c - 15) mod 26")
    text = input("Enter affine ciphertext: ")
    print("Possible plaintext:", decrypt(text, a, b))

if __name__ == "__main__":
    main()
