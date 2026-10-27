# Experiment 5: Affine Caesar Cipher
# Formula: C = (a*p + b) mod 26.
# For one-to-one encryption, gcd(a, 26) must equal 1. b may be any integer;
# it is reduced modulo 26, so values 0 through 25 are sufficient.

from math import gcd

def encrypt(text, a, b):
    result = ""
    for ch in text:
        if ch.isupper():
            p = ord(ch) - ord("A")
            result += chr(((a * p + b) % 26) + ord("A"))
        elif ch.islower():
            p = ord(ch) - ord("a")
            result += chr(((a * p + b) % 26) + ord("a"))
        else:
            result += ch
    return result

def main():
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
    except ValueError:
        print("Please enter integer keys.")
        return
    if gcd(a, 26) != 1:
        print("Invalid a: gcd(a, 26) must be 1.")
        print("Allowed a values modulo 26: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25")
        return
    text = input("Enter plaintext: ")
    print("Ciphertext:", encrypt(text, a, b))

if __name__ == "__main__":
    main()
