from math import gcd
def egcd(a,b):
 if not b:return a,1,0
 g,x,y=egcd(b,a%b);return g,y,x-(a//b)*y
n,e=3599,31;p=None
for x in range(2,int(n**.5)+1):
 if n%x==0:p=x;break
if p is None:print("No factor found")
else:
 q=n//p;phi=(p-1)*(q-1);g,x,_=egcd(e,phi);d=x%phi
 print("p =",p,"q =",q);print("phi(n) =",phi);print("Private exponent d =",d);print("Private key (d,n) =", (d,n));print("Check:",e*d%phi)
