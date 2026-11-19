"""Exact finite checks for SA20 Part B; no random sampling.

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 2026-11-19.
The program checks the three-point semigroup counterexample to 155/002,
the F2 subset F4 tensor-kernel counterexample to 153/004, and a bounded
arithmetic certificate for divided-power structure constants.
"""
from itertools import product
from math import factorial, comb
from time import perf_counter

started = perf_counter()
# S={a,b,z}; z is absorbing and a*b=z.
table = ((0, 2, 2), (2, 1, 2), (2, 2, 2))
elts = list(product(range(2), repeat=3))
zero = (0, 0, 0)
one_A = (1, 1, 1)
one_U = (1, 1, 1)  # e_a+e_b-e_z in characteristic two
def add(x, y): return tuple(a ^ b for a, b in zip(x, y))
def mulA(x, y): return tuple(a & b for a, b in zip(x, y))
def mulU(x, y):
    out = [0, 0, 0]
    for i, j in product(range(3), repeat=2):
        out[table[i][j]] ^= x[i] & y[j]
    return tuple(out)
def augU(x): return sum(x) % 2
def delta(x): return tuple(x[table[i][j]] for i,j in product(range(3),repeat=2))
def counitA(x): return sum(x) % 2
assert all(table[table[i][j]][k] == table[i][table[j][k]]
           for i,j,k in product(range(3),repeat=3))
assert all(table[i][j] == table[j][i] for i,j in product(range(3),repeat=2))
assert all(mulU(one_U,x) == x == mulU(x,one_U) for x in elts)
assert all(mulU(mulU(x,y),z) == mulU(x,mulU(y,z))
           for x,y,z in product(elts,repeat=3))
assert all(augU(mulU(x,y)) == augU(x)*augU(y) for x,y in product(elts,repeat=2))
assert augU(one_U) == 1
assert delta(one_A) == (1,)*9
assert all(delta(mulA(x,y)) == mulA(delta(x),delta(y)) for x,y in product(elts,repeat=2))
assert all(tuple(sum(delta(x)[3*i+j] for i in range(3))%2 for j in range(3)) == x for x in elts)
assert all(tuple(sum(delta(x)[3*i+j] for j in range(3))%2 for i in range(3)) == x for x in elts)
ea, eb = (1,0,0), (0,1,0)
assert counitA(mulA(ea,eb)) == 0
assert counitA(ea)*counitA(eb) == 1
unit_candidates = [s for s in range(3) if all(table[s][t] == t == table[t][s] for t in range(3))]
assert not unit_candidates
print('B.002: F2^3 / three-element meet semigroup')
print('  U elements:',len(elts),'; associativity triples:',len(elts)**3)
print('  augmentation pairs:',len(elts)**2,'; coproduct multiplicativity pairs:',len(elts)**2)
print('  coalgebra counit tests:',2*len(elts),'; potential one-dimensional tensor units:',len(unit_candidates))
print('  epsilon_A(e_a e_b)=0, epsilon_A(e_a) epsilon_A(e_b)=1: PASS')

# F4 = F2[alpha]/(alpha^2+alpha+1), encoded as 0,1,alpha,alpha+1.
def f4mul(x,y):
    raw = 0
    for i,j in product(range(2),repeat=2):
        if (x>>i)&1 and (y>>j)&1: raw ^= 1<<(i+j)
    if raw & 4: raw ^= 7
    return raw
assert all(f4mul(x,y) == f4mul(y,x) for x,y in product(range(4),repeat=2))
assert all(f4mul(f4mul(x,y),z) == f4mul(x,f4mul(y,z))
           for x,y,z in product(range(4),repeat=3))
assert all(any(f4mul(x,y)==1 for y in range(4)) for x in range(1,4))
alpha = 2
# On span_F2(q,alpha*q) tensor itself, coefficients are four independent bits.
def tensor_image(t):
    coeffs = (1,alpha,alpha,f4mul(alpha,alpha))
    v=0
    for bit,c in zip(t,coeffs):
        if bit: v ^= c
    return v
tensors=list(product(range(2),repeat=4))
kernel=[t for t in tensors if tensor_image(t)==0]
assert len(kernel)==4
witness=(0,1,1,0)
assert witness != (0,)*4 and tensor_image(witness)==0
print('B.008: F2 subset F4, q=T^2-T')
print('  Tensor subspace elements:',len(tensors),'; image elements:',len({tensor_image(t) for t in tensors}),'; kernel elements:',len(kernel))
print('  q tensor alpha*q + alpha*q tensor q is nonzero but polynomial image zero: PASS')

checked=0
for m,n in product(range(1,13),repeat=2):
    numerator=factorial(m*n)
    denominator=factorial(m)*factorial(n)**m
    assert numerator%denominator==0
    checked+=1
multi=0
for rs in product(range(7),repeat=5):
    m=sum(rs)
    if not 1<=m<=6: continue
    n=sum((i+1)*r for i,r in enumerate(rs))
    den=1
    for i,r in enumerate(rs): den*=factorial(r)*factorial(i+1)**r
    assert factorial(n)%den==0
    multi+=1
print('B.006: divided-power coefficients')
print('  pure compositions gamma_m(gamma_n):',checked,'pairs, 1<=m,n<=12')
print('  multivariate Bell coefficients:',multi,'multiplicity vectors, five block sizes, at most six blocks')
print('  all coefficients integral: PASS')

# P=F2[T]/((T^2-T)^3), a finite analyser but no compatible plethory.
# Bit i is the coefficient of T^i. Modulus = T^6+T^5+T^4+T^3.
modulus = sum(1<<i for i in (3,4,5,6))
def pmul(x,y):
    z=0
    for i in range(6):
        if (y>>i)&1: z ^= x<<i
    while z.bit_length()>6:
        z ^= modulus << (z.bit_length()-7)
    return z
P=range(64)
mul_table=[[pmul(x,y) for y in P] for x in P]
powers=[[1] for x in P]
for x in P:
    for i in range(1,7): powers[x].append(mul_table[powers[x][-1]][x])
def pcomp(f,g):
    out=0
    for i in range(6):
        if (f>>i)&1: out ^= powers[g][i]
    return out
ct=[[pcomp(f,g) for g in P] for f in P]
assert all(ct[2][x]==x==ct[x][2] for x in P)
assert all(ct[1][x]==1 for x in P)
triple_count=0
for f,g,h in product(P,repeat=3):
    assert ct[ct[f][g]][h]==ct[f][ct[g][h]]
    assert ct[f^g][h]==(ct[f][h]^ct[g][h])
    assert ct[mul_table[f][g]][h]==mul_table[ct[f][h]][ct[g][h]]
    triple_count+=1
# Optional 3 is checked using standard polynomial coefficients for each f.
decomp_count=0
for f in P:
    plus=[(i,j) for n in range(6) if (f>>n)&1
          for i in range(n+1) for j in [n-i] if comb(n,i)%2]
    times=[(i,i) for i in range(6) if (f>>i)&1]
    for g,h in product(P,repeat=2):
        vp=0
        for i,j in plus: vp ^= mul_table[powers[g][i]][powers[h][j]]
        vm=0
        for i,j in times: vm ^= mul_table[powers[g][i]][powers[h][j]]
        assert vp==ct[f][g^h]
        assert vm==ct[f][mul_table[g][h]]
        decomp_count+=1
constants=[f for f in P if all(ct[f][g]==f for g in P)]
assert constants==[0,1]
q=(1<<2)|(1<<1)
q2=mul_table[q][q]
assert mul_table[q2][q]==0
# tensor sum q^2(X)q(Y)+q(X)q^2(Y) in basis T^i tensor T^j.
def tensor(a,b):
    z=0
    for i,j in product(range(6),repeat=2):
        if (a>>i)&1 and (b>>j)&1: z ^= 1<<(6*i+j)
    return z
bad=tensor(q2,q)^tensor(q,q2)
assert bad!=0
print('B.011: P=F2[T]/((T^2-T)^3)')
print('  elements:',len(P),'; all composition/distributivity triples:',triple_count)
print('  both optional decomposition identities checked for all (F,G,H):',decomp_count)
print('  constant elements:',constants,'; nonzero forced coproduct of zero: tensor_bitmask=',bad)
print('  analyser axioms 1--3 hold; compatible biring impossible: PASS')
print('elapsed_seconds=%.6f'%(perf_counter()-started))
