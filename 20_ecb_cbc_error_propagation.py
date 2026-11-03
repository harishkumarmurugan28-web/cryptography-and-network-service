print("ECB ciphertext error: only the corresponding plaintext block is corrupted.")
print("CBC transmission error in C1: P1 is corrupted; the corresponding bit in P2 flips.")
print("P3 onward is unaffected by a single transmission bit error in C1.")
print("A source error in P1 changes C1 and can affect all later ciphertext blocks through chaining.")
