from math import gcd

def inv(a, m=26):
    for x in range(m):
        if a * x % m == 1:
            return x
    raise ValueError("No inverse")

def inverse(K):
    a, b = K[0]
    c, d = K[1]
    det = (a * d - b * c) % 26

    if gcd(det, 26) != 1:
        raise ValueError("Key not invertible")

    z = inv(det)
    return [[z * d % 26, (-z * b) % 26],
            [(-z * c) % 26, z * a % 26]]

def run(text, M):
    t = ''.join(x for x in text.upper() if x.isalpha())
    if len(t) % 2:
        t += 'X'

    out = ''
    for i in range(0, len(t), 2):
        x, y = ord(t[i]) - 65, ord(t[i + 1]) - 65
        out += chr((M[0][0] * x + M[0][1] * y) % 26 + 65)
        out += chr((M[1][0] * x + M[1][1] * y) % 26 + 65)
    return out

print("Enter the 2x2 key matrix:")
K = [
    list(map(int, input("Enter row 1 (two numbers): ").split())),
    list(map(int, input("Enter row 2 (two numbers): ").split()))
]

msg = input("Enter plaintext: ")

try:
    c = run(msg, K)
    ki = inverse(K)

    print("Plaintext:", msg)
    print("Ciphertext:", c)
    print("Inverse key:", ki)
    print("Decrypted:", run(c, ki))

except ValueError as e:
    print("Error:", e)