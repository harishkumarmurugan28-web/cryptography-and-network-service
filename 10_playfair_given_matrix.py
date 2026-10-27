# Experiment 10: Playfair Encryption Using the Given Matrix
# Matrix:
# M F H I/J K
# U N O P Q
# Z V W X Y
# E L A R G
# D S T B C

def encrypt_with_matrix(text):
    matrix = [
        list("MFHIK"),
        list("UNOPQ"),
        list("ZVWXY"),
        list("ELARG"),
        list("DSTBC")
    ]
    positions = {matrix[r][c]: (r, c) for r in range(5) for c in range(5)}
    cleaned = "".join(ch for ch in text.upper() if ch.isalpha()).replace("J", "I")
    pairs = []
    i = 0
    while i < len(cleaned):
        a = cleaned[i]
        if i + 1 >= len(cleaned):
            b, i = "X", i + 1
        elif cleaned[i + 1] == a:
            b, i = "X", i + 1
        else:
            b, i = cleaned[i + 1], i + 2
        pairs.append((a, b))

    result = ""
    for a, b in pairs:
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
    message = "Must see you over Cadogan West. Coming at once."
    print("Plaintext:", message)
    print("Ciphertext:", encrypt_with_matrix(message))

if __name__ == "__main__":
    main()
