# Experiment 9: Decrypt a Playfair Cipher Message (PT-109)
# Aim: Decrypt a Playfair ciphertext using a 5x5 matrix generated from a keyword.
# The question does not specify the keyword/matrix, so enter the key supplied by
# your instructor or textbook.

def make_matrix(key):
    sequence = ""
    for ch in (key + "ABCDEFGHIKLMNOPQRSTUVWXYZ").upper().replace("J", "I"):
        if ch.isalpha() and ch not in sequence:
            sequence += ch
    sequence = sequence.replace("J", "")
    return [list(sequence[i:i+5]) for i in range(0, 25, 5)]

def decrypt(ciphertext, key):
    matrix = make_matrix(key)
    positions = {matrix[r][c]: (r, c) for r in range(5) for c in range(5)}
    text = "".join(ch for ch in ciphertext.upper() if ch.isalpha()).replace("J", "I")
    if len(text) % 2:
        raise ValueError("Playfair ciphertext must contain an even number of letters.")
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = positions[a]
        r2, c2 = positions[b]
        if r1 == r2:
            result += matrix[r1][(c1 - 1) % 5]
            result += matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 - 1) % 5][c1]
            result += matrix[(r2 - 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]
    return result

def main():
    ciphertext = """KXJEY UREBE ZWEHE WRYTU HEYFS
KREHE GOYFI WTTTU OLKSY CAJPO
BOTEI ZONTX BYBNT GONEY CUZWR
GDSON SXBOU YWRHE BAAHY USEDQ"""
    key = input("Enter Playfair keyword: ")
    print("Decrypted text:", decrypt(ciphertext, key))

if __name__ == "__main__":
    main()
