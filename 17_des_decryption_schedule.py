keys=[f"K{i}" for i in range(1,17)]
print("DES encryption round keys:", " ".join(keys))
print("DES decryption round keys:", " ".join(reversed(keys)))
print("DES decryption uses the same round function and subkeys in reverse order: K16,...,K1.")
