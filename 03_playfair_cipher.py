# Experiment 3: Playfair Cipher
# Aim: Encrypt plaintext two letters at a time using a 5x5 keyword matrix.
# I and J share one cell. X is used as a filler when required.

import string

def make_matrix(key):
    sequence = ""
    for ch in (key + string.ascii_uppercase).upper().replace("J", "I"):
        if ch.isalpha() and ch not in sequence:
            sequence += ch
    sequence = sequence.replace("J", "")
    return [list(sequence[i:i + 5]) for i in range(0, 25, 5)]

def prepare_pairs(text):
    text = "".join(ch for ch in text.upper() if ch.isalpha()).replace("J", "I")
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 >= len(text):
            b = "X"
            i += 1
        elif text[i + 1] == a:
            b = "X"
            i += 1
        else:
            b = text[i + 1]
            i += 2
        pairs.append((a, b))
    return pairs

def encrypt(text, key):
    matrix = make_matrix(key)
    positions = {matrix[r][c]: (r, c) for r in range(5) for c in range(5)}
    result = ""
    for a, b in prepare_pairs(text):
        r1, c1 = positions[a]
        r2, c2 = positions[b]
        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]
    return result

def main():
    key = input("Enter keyword: ")
    text = input("Enter plaintext: ")
    print("Ciphertext:", encrypt(text, key))

if __name__ == "__main__":
    main()
