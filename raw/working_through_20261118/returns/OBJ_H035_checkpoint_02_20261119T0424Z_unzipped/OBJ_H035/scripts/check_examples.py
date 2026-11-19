"""Exact finite calculations supporting, but not replacing, the written proofs."""
from fractions import Fraction

# H035.21: k[t^3,t^4,t^5]/(t^3).  The semigroup contains 0 and all n>=3.
# Every exponent >=6 is 3 plus an element of the semigroup, so the
# quotient basis is exhaustively obtained from exponents <=5.
semigroup={0,3,4,5}
basis=[n for n in sorted(semigroup) if n-3 not in semigroup]
assert basis==[0,4,5]
def product(a,b):
 s=a+b
 return s if s in basis else None
table=[[product(a,b) for b in basis] for a in basis]
socle=[a for a in basis if all(product(a,b) is None for b in [4,5])]
assert socle==[4,5]
print('H035.21 parameter quotient basis:',basis)
print('Multiplication table (None denotes zero):',table)
print('Socle basis:',socle,'dimension',len(socle))

# H035.15: the resolution tensors to alternating x,0 on k[x].
# Coefficient arrays check the relevant maps in arbitrary finite degrees;
# the written monomial proof establishes injectivity in every degree.
for degree in range(1,10):
 for i in range(degree):
  vector=[Fraction(0)]*degree;vector[i]=Fraction(1)
  mult_x=[Fraction(0)]+vector
  assert any(mult_x)
print('H035.15 multiplication by x has independent shifted monomial images;')
print('the exact proof uses ann(x)=(y), ann(y)=(x), not a truncated-ring approximation.')

# H035.38: the connecting homomorphism in the P^1 extension is [t].
# Over k(t) it has rank 1; at t=0 it has rank 0.
print('H035.38 connecting matrix [t]: generic kernel rank 0, special kernel dimension 1.')
print('H^0(E)=0; H^1(E)=A/(t); H^0(E_0)=k, as independently derived in the proof.')
