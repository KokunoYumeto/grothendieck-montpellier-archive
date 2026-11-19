"""Exact finite checks for Part D. No floating point or external data.

Run: python RESEARCH_SA05_work/part_d/check_part_d.py
Output is archived alongside this script as checks_output.txt.
"""
from itertools import permutations, product
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

x = s.symbols('x')
f = x**4-x-1
print('D.2(b): f =', f, '; discriminant =', s.discriminant(f, x))
for p in [2, 3, 7]:
    print('factor mod', p, ':', s.factor_list(f, modulus=p))

def compose(a,b):
    return tuple(a[b[i]] for i in range(len(a)))
def inv(a):
    return tuple(a.index(i) for i in range(len(a)))
def generated(gens,n=4):
    identity=tuple(range(n)); seen={identity}; queue=[identity]
    while queue:
        a=queue.pop()
        for b in gens:
            c=compose(a,b)
            if c not in seen: seen.add(c); queue.append(c)
    return seen
def derived(group):
    comms={compose(compose(compose(a,b),inv(a)),inv(b)) for a in group for b in group}
    return generated(comms)
S4=set(permutations(range(4))); A4=derived(S4); V4=derived(A4)
print('Derived series group orders:',len(S4),len(A4),len(V4),len(derived(V4)))
assert [len(S4),len(A4),len(V4),len(derived(V4))] == [24,12,4,1]

print('\nD.1: CM quadratic twists at 5')
for a in [-1,-4]:
    pts=[(u,v) for u,v in product(range(5),repeat=2) if (v*v-u**3-a*u)%5==0]
    count=len(pts)+1
    print(f'y^2=x^3+({a})x: affine points={pts}; total={count}; trace={6-count}; discriminant={-64*a**3}')
assert sum((v*v-u**3+u)%5==0 for u,v in product(range(5),repeat=2))+1 == 8
assert sum((v*v-u**3+4*u)%5==0 for u,v in product(range(5),repeat=2))+1 == 4

print('\nD.3: Q(sqrt(5)), minimal polynomial of (1+sqrt(5))/2 modulo 2')
print(s.factor_list(x*x-x-1,modulus=2))
for r in range(1,6):
    vectors=[eps for eps in product(range(2),repeat=r) if sum(eps)%2==0]
    print('r=',r,'even sign vectors=',vectors)
    assert len(vectors)==2**(r-1)

print('\nD.4: reflex matrices (all Galois translates as columns)')
def cyclic_matrix(n,Phi):
    return s.Matrix([[int((i-j)%n in Phi) for j in range(n)] for i in range(n)])
for label,n,Phi in [('imaginary quadratic',2,{0}),('primitive cyclic quartic',4,{0,1}),
                    ('primitive cyclic sextic',6,{0,1,2}),('induced cyclic sextic',6,{0,2,4})]:
    A=cyclic_matrix(n,Phi)
    print(label,'type=',sorted(Phi),'matrix=',A.tolist(),'rank=',A.rank(),
          'Smith=',[smith_normal_form(A,domain=s.ZZ)[i,i] for i in range(n)])
    print('character relations=',[list(v) for v in A.T.nullspace()])
G=list(product(range(2),repeat=2)); Phi={(0,0),(0,1)}
A=s.Matrix([[int((a[0]^b[0],a[1]^b[1]) in Phi) for b in G] for a in G])
print('biquadratic quartic, c=(1,0), type=',sorted(Phi),'matrix=',A.tolist(),'rank=',A.rank())
assert A.rank()==2

print('\nD.1: residual reflex obstruction for Q(zeta_5) at p=2, q=4')
G=[1,2,3,4]; c=4; types=[]
for vals in product([1,4],[2,3]):
    Phi=set(vals)
    stabilizer=[g for g in G if {g*a%5 for a in Phi}==Phi]
    types.append((sorted(Phi),stabilizer))
print('CM types and stabilizers:',types)
assert all(stab==[1] for _,stab in types)
print('Order of 2 mod 5 =',next(n for n in range(1,5) if pow(2,n,5)==1))
print('Every reflex field is Q(zeta_5), whose residue field at 2 has degree 4; F_16 does not embed into F_4.')
print('minimal polynomial of pi=2*zeta_5:',s.expand(16*((x/2)**4+(x/2)**3+(x/2)**2+x/2+1)))

print('\nD.1: the square admits a CM type with the correct reflex residue field')
G=list(product(range(4),range(2)))
def add(a,b): return ((a[0]+b[0])%4,(a[1]+b[1])%2)
c=(2,1); frob=(1,1)
Delta={((j*frob[0])%4,(j*frob[1])%2) for j in range(4)}
Phi={a for a in G if a[1]==0}
H={a for a in G if {add(a,b) for b in Phi}==Phi}
assert {add(c,a) for a in Phi} == set(G)-Phi
cosets=[]; seen=set()
for a in G:
    coset={add(d,a) for d in Delta}
    if a not in seen: cosets.append(coset);seen |= coset
print('G=C4 x C2; c=',c,'; Frobenius=',frob,'; decomposition=',sorted(Delta))
print('type induced from Q(sqrt(-3))=',sorted(Phi),'; stabilizer=',sorted(H))
print('type counts on decomposition orbits=',[(len(Phi&z),len(z)) for z in cosets])
print('reflex residue degree=',len(Delta)//len(Delta&H))
assert all(len(Phi&z)*2==len(z) for z in cosets)
assert len(Delta)//len(Delta&H)==2
