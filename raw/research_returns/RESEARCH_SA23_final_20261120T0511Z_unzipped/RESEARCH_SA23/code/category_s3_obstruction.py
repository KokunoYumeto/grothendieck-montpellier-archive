from itertools import permutations
from time import perf_counter
start=perf_counter()
G=list(permutations(range(3)))
def mul(a,b):return tuple(a[b[i]] for i in range(3))
def sign(a):return (-1)**sum(a[i]>a[j] for i in range(3) for j in range(i+1,3))
e=(0,1,2);center=[a for a in G if all(mul(a,b)==mul(b,a) for b in G)]
assert center==[e]
checks=0
for a in G:
 for b in G:
  assert mul(a,b) in G
  assert sign(mul(a,b))==sign(a)*sign(b)
  for c in G:
   assert mul(mul(a,b),c)==mul(a,mul(b,c));checks+=1
r=(1,2,0);s=(0,2,1)
assert mul(mul(s,r),s)==mul(r,r)
assert sign(r)==1 and sign(s)==-1
# x^2+x+1 has no residue root, hence is irreducible over F_5.
quad=[(x*x+x+1)%5 for x in range(5)]
assert all(quad)
# x^3-5 is Eisenstein at 5 (coefficient checks).
coef=[-5,0,0,1]
assert all(c%5==0 for c in coef[:-1]) and coef[0]%25!=0 and coef[-1]%5!=0
# The sign vector in the regular representation is fixed by the center,
# while an unramified Frobenius (s) acts on it by -1.
v={g:sign(g) for g in G}
for g in G:
 assert v[mul(s,g)]==-v[g]
 assert v[mul(e,g)]==v[g]
print('S3 elements:',G)
print('center:',center)
print('all group closure/sign products checked:',len(G)**2)
print('associativity triples checked:',checks)
print('s r s = r^2; sign(r)=+1; sign(s)=-1: verified')
print('x^2+x+1 values mod 5:',quad,'(no root)')
print('x^3-5 Eisenstein coefficient checks: verified')
print('regular sign-vector action: center +1, unramified quotient Frobenius -1')
print('Wall seconds:',perf_counter()-start)
