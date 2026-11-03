# Educational S-DES CBC; 8-bit blocks, 10-bit key.
P10=[3,5,2,7,4,10,1,9,8,6];P8=[6,3,7,4,8,5,10,9];IP=[2,6,3,1,4,8,5,7];IPI=[4,1,3,5,7,2,8,6];EP=[4,1,2,3,2,3,4,1];P4=[2,4,3,1]
S0=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]];S1=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
def perm(x,t,n):return sum(((x>>(n-p))&1)<<(len(t)-1-i) for i,p in enumerate(t))
def rot(x,n):return ((x<<n)|(x>>(5-n)))&31
def keys(k):
 x=perm(k,P10,10);l=x>>5;r=x&31;l=rot(l,1);r=rot(r,1);a=perm(l<<5|r,P8,10);l=rot(l,2);r=rot(r,2);return a,perm(l<<5|r,P8,10)
def fk(x,k):
 l=x>>4;r=x&15;e=perm(r,EP,4)^k
 def sb(v,S):return S[((v&8)>>2)|(v&1)][(v>>1)&3]
 z=sb(e>>4,S0)*4+sb(e&15,S1);return ((l^perm(z,P4,4))<<4)|r
def crypt(x,k,rev=False):
 a,b=keys(k);x=perm(x,IP,8);x=fk(x,b if rev else a);x=((x&15)<<4)|(x>>4);x=fk(x,a if rev else b);return perm(x,IPI,8)
k=int(input("10-bit key binary: "),2);iv=int(input("8-bit IV binary: "),2);blocks=[int(x,2) for x in input("Plaintext blocks (8-bit binary separated by spaces): ").split()]
cs=[];prev=iv
for p in blocks:prev=crypt(p^prev,k);cs.append(prev)
print("Ciphertext:"," ".join(f"{x:08b}" for x in cs));out=[];prev=iv
for c in cs:out.append(crypt(c,k,True)^prev);prev=c
print("Decrypted:"," ".join(f"{x:08b}" for x in out))
