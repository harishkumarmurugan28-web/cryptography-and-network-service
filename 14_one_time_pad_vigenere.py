def clean(s):return ''.join(c.lower() for c in s if c.isalpha())
def enc(s,key):
 s=clean(s)
 if len(s)!=len(key):raise ValueError("Key length must match letter count")
 return ''.join(chr((ord(c)-97+k)%26+97) for c,k in zip(s,key))
def derive(plain,cipher):
 p,c=clean(plain),clean(cipher)
 return [(ord(y)-ord(x))%26 for x,y in zip(p,c)]
p="send more money";key=[9,0,1,7,23,15,21,14,11,11,2,8,9]
c=enc(p,key);print("(a) Ciphertext:",c)
print("(b) Key stream to make this ciphertext decrypt as 'cash not needed':",derive("cash not needed",c))
