# Experiment 1: Caesar Cipher
# Aim: Encrypt plaintext by shifting each alphabetic character k positions.

def caesar_encrypt(text, k):
    result = ""
    for ch in text:
        if "A" <= ch <= "Z":
            result += chr((ord(ch) - ord("A") + k) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            result += chr((ord(ch) - ord("a") + k) % 26 + ord("a"))
        else:
            result += ch
    return result

def main():
    text = input("Enter plaintext: ")
    try:
        k = int(input("Enter key (1-25): "))
    except ValueError:
        print("Invalid key!")
        return
    if not 1 <= k <= 25:
        print("Invalid key! Enter a value from 1 to 25.")
        return
    print("Ciphertext:", caesar_encrypt(text, k))

if __name__ == "__main__":
    main()
