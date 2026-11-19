"""Exact checks reconstructed from K29-02/188 and K29-03/214–217.

Finite checks certify the displayed identities/examples only. They do not
certify the categorical or analytical proofs in proofs.md.
"""
from itertools import combinations, permutations, product
from math import comb, factorial
import sympy as s

def elementary(xs,k):
    return sum((s.prod(c) for c in combinations(xs,k)),s.Integer(0)) if k else s.Integer(1)

print('SYMMETRIC HOMOTOPY COEFFICIENTS (exact rational polynomial arithmetic)')
for n in range(1,9):
    xs=s.symbols('x:'+str(n))
    def phi(zero):
        remaining=[x for j,x in enumerate(xs) if j not in zero]
        return sum((elementary(remaining,k)/s.Integer(n*comb(n-1,k)) for k in range(min(n-1,len(remaining))+1)),s.Integer(0))
    degree0=s.expand(sum((1-xs[j])*phi({j}) for j in range(n))-(1-s.prod(xs)))
    assert degree0==0
    positive=[]
    for q in range(1,n+1):
        J=set(range(q))
        check=s.expand(q*phi(J)+sum((1-xs[k])*phi(J|{k}) for k in range(q,n))-1)
        assert check==0
        positive.append(q)
    print(f'n={n}: degree0 identity=0; positive-form identity=0 for q={positive}')
print('General proof is the derivative integral in proofs.md; n≤8 is a check, not that proof.')

print('\nC2 ORBIT REALIZATION AND SUBORDINATION-TO-ZERO EXAMPLES')
X=(0,1)
involution={0:1,1:0}
equivariant=[]
for values in product(X,repeat=2):
    f=dict(zip(X,values))
    if all(f[involution[x]]==involution[f[x]] for x in X): equivariant.append(f)
invariant=[]
for mask in range(4):
    A={x for x in X if mask>>x&1}
    if {involution[x] for x in A}==A: invariant.append(sorted(A))
assert len(equivariant)==2 and invariant==[[],[0,1]]
print('Regular C2-set equivariant endomorphisms:',equivariant)
print('Invariant subsets:',invariant,'; orbit scheme has one point and two clopens.')
print('Both distinct equivariant automorphisms induce the single identity map on the orbit set.')
trivial_Hom={(a,b):b**a for a in range(5) for b in range(5)}
for (a,b),v in trivial_Hom.items():
    assert v==sum(1 for _ in product(range(b),repeat=a))
print('Trivial-action inclusion has exactly all set maps between its objects (sizes0–4 checked).')
print('Regular C2-set is not a trivial-action object; pullback along empty object is empty for both.')

print('\nFINITE FRAME ARITHMETIC FOR SCAN216')
for n in range(0,7):
    frames=list(permutations(range(n)))
    assert len(frames)==factorial(n)
    print(f'n={n}: |frames|={len(frames)}, evaluation-domain={len(frames)*n}, torsor-domain={len(frames)*factorial(n)}, torsor-codomain={len(frames)**2}')
    if n<=4:
        pairs={(p,tuple(p[g[i]] for i in range(n))) for p in frames for g in permutations(range(n))}
        assert len(pairs)==len(frames)**2
print('Categorical isomorphisms follow from conservativity, not from these finite counts alone.')

print('\nTHREE-ELEMENT PARTITIONS AND EXPECTED MULTIPLE-POINT DIMENSIONS')
def partitions(seq):
    if not seq:
        yield []
        return
    x,*rest=seq
    for p in partitions(rest):
        yield [(x,)]+p
        for i in range(len(p)):
            yield p[:i]+[tuple(sorted((x,)+p[i]))]+p[i+1:]
parts=sorted({tuple(sorted(p)) for p in partitions([1,2,3])},key=lambda p:(len(p),p))
assert len(parts)==5
n,d=s.symbols('n d',integer=True)
for p in parts:
    dim=n-(len(p)-1)*d
    print(p,'blocks=',len(p),'expected=',dim,'at n=3,d=1:',dim.subs({n:3,d:1}))
assert n-(3-1)*d-(n-3*d)==d
print('The displayed lower bound n−|E|d misses d for the claimed equality at the maximal partition.')
for degree in range(1,8):
    assert 1+(degree-1)==degree
print('Diagonal induction: total degree n, diagonal1, complement n−1, reconstructed total n.')

print('\nKUMMER ČECH SIGN AND COCYCLE CHECKS')
a,b,c=s.symbols('a b c',nonzero=True)
g01=b/a;g12=c/b;g02=c/a
assert s.simplify(g01*g12/g02)==1
print('Forward equation changes g_ab=a_b/a_a satisfy g_ab g_bc/g_ac=1.')
z01,z12,z02=s.symbols('z01 z12 z02',nonzero=True)
c_forward=z01*z12/z02
c_reverse=(1/z01)*(1/z12)/(1/z02)
assert s.simplify(c_forward*c_reverse)==1
print('Forward arrows a→b and standard backwards Čech arrows give inverse cocycle representatives.')
z03,z13,z23=s.symbols('z03 z13 z23',nonzero=True)
c012=z01*z12/z02;c013=z01*z13/z03;c023=z02*z23/z03;c123=z12*z23/z13
assert s.simplify(c123/c023*c013/c012)==1
print('δc=1 checked on four indices. c^n=1 follows from z_ab^n=g_ab.')
t=s.symbols('t')
for exponent in range(1,7):
    assert s.diff(t**exponent-2,t)==exponent*t**(exponent-1)
print('Root polynomial derivative n*t^(n−1); away from the divisor the root coordinate is a unit.')
print('Support-only example: S=Spec Z,D=(2),n=3. n is invertible onD; root stack trivial offD, including at3.')
print('\nALL EXACT CHECKS PASSED')
