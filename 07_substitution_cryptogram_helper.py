# Experiment 7: Simple Substitution Cipher Cryptogram Helper
# Aim: Assist manual frequency analysis and substitution decryption.
# Enter substitutions as ciphertext-symbol=plaintext-letter, separated by spaces.
# Example: A=e B=t C=h
# Non-letter symbols in the supplied cryptogram are retained unless mapped.

from collections import Counter

CIPHERTEXT = """53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83
(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*
;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81
(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"""

def show_frequencies(text):
    counts = Counter(ch for ch in text if not ch.isspace())
    print("Cipher symbol frequencies:")
    for symbol, count in counts.most_common():
        print(repr(symbol), ":", count)

def main():
    print("Cryptogram frequency analysis and manual substitution helper")
    show_frequencies(CIPHERTEXT)
    raw = input("Enter mappings (cipher-symbol=plaintext-letter), or press Enter to skip: ")
    mapping = {}
    for item in raw.split():
        if "=" in item:
            cipher_symbol, plain_symbol = item.split("=", 1)
            if len(cipher_symbol) == 1 and len(plain_symbol) == 1:
                mapping[cipher_symbol] = plain_symbol
    decoded = "".join(mapping.get(ch, ch) for ch in CIPHERTEXT)
    print("\\nPartially decoded text:")
    print(decoded)
    print("\\nNote: This is a monoalphabetic cryptogram; use frequency, repeated patterns,")
    print("and likely words such as THE to infer further symbol mappings.")

if __name__ == "__main__":
    main()
