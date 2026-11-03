from math import gcd
M=26
def inv(a):
 for x in range(M):
  if a*x%M==1:return x
 raise ValueError("determinant has no inverse modulo 26")
def inverse(A):
 a,b=A[0];c,d=A[1];det=(a*d-b*c)%M
 if gcd(det,M)!=1:raise ValueError("Choose plaintext blocks with invertible matrix")
 z=inv(det);return [[z*d%M,(-z*b)%M],[(-z*c)%M,z*a%M]]
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2))%M for j in range(2)] for i in range(2)]
def dig(s):return [ord(x.upper())-65 for x in s]
p1=input("Plaintext digraph 1: ");p2=input("Plaintext digraph 2: ")
c1=input("Ciphertext digraph 1: ");c2=input("Ciphertext digraph 2: ")
if not all(len(x)==2 and x.isalpha() for x in (p1,p2,c1,c2)): print("Each input must be two letters.")
else:
 P=[[dig(p1)[0],dig(p2)[0]],[dig(p1)[1],dig(p2)[1]]]
 C=[[dig(c1)[0],dig(c2)[0]],[dig(c1)[1],dig(c2)[1]]]
 try: print("Recovered Hill key:",mul(C,inverse(P)))
 except ValueError as e: print(e)
