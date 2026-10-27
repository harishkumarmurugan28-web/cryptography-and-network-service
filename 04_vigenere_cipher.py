# Experiment 4: Polyalphabetic Substitution (Vigenere) Cipher
# Aim: Encrypt each plaintext letter using a shift determined by a repeating keyword.

def encrypt(text, key):
    key = key.upper()
    result = ""
    j = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - ord("A")
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + shift) % 26 + base)
            j += 1
        else:
            result += ch
    return result

def main():
    text = input("Enter plaintext: ")
    key = input("Enter alphabetic key: ")
    if not key.isalpha():
        print("Invalid key! Use letters only.")
        return
    print("Ciphertext:", encrypt(text, key))

if __name__ == "__main__":
    main()
