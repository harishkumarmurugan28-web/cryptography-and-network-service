from math import gcd
n=int(input("RSA modulus n: "));m=int(input("Plaintext block m (integer): "));g=gcd(m,n)
print("gcd(m,n) =",g)
if 1<g<n:print("A nontrivial factor is revealed:",g,"and",n//g,". RSA modulus is factored.")
elif g==n:print("m is a multiple of n; no proper factor revealed.")
else:print("gcd is 1; this block does not reveal a factor using gcd.")
