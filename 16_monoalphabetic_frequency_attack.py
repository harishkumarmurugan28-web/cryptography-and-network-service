from collections import Counter
ORDER="ETAOINSHRDLCUMWFGYPBVKJXQZ"
s=input("Ciphertext: ");top=max(1,int(input("Top candidates (e.g. 10): ")))
counts=Counter(c.upper() for c in s if c.isalpha());cipher_order=[c for c,_ in counts.most_common()]
mapping={c:ORDER[i] for i,c in enumerate(cipher_order) if i<len(ORDER)}
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":mapping.setdefault(c,c)
out=''.join(mapping.get(c.upper(),c).lower() if c.islower() else mapping.get(c,c) for c in s)
print("Frequency-based candidate (heuristic):");print(out)
print("This basic version produces one candidate, not a reliable ranked list of",top,"solutions.")
