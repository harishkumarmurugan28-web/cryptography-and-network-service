EN=[8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,.153,.772,4.025,2.406,6.749,7.507,1.929,.095,5.987,6.327,9.056,2.758,.978,2.36,.15,1.974,.074]
def dec(s,k):
 return ''.join(chr((ord(c.upper())-65-k)%26+65) if c.isalpha() else c for c in s)
def score(s):
 letters=[ord(c.upper())-65 for c in s if c.isalpha()];n=len(letters)
 if not n:return -1e9
 counts=[letters.count(i) for i in range(26)]
 return -sum((counts[i]-n*EN[i]/100)**2/(n*EN[i]/100+1e-9) for i in range(26))
s=input("Ciphertext: ");top=max(1,int(input("Top candidates (e.g. 10): ")))
for i,(sc,k,t) in enumerate(sorted([(score(dec(s,k)),k,dec(s,k)) for k in range(26)],reverse=True)[:top],1):print(f"{i}. shift={k}: {t}")
