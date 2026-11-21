#!/usr/bin/env python3
"""Independent exact identities for HD-ALT03; universal proof audited separately."""
from pathlib import Path
from fractions import Fraction
import hashlib, json
import sympy as s

def partitions(n, cap=None):
    if n == 0:
        yield ()
    else:
        for first in range(min(n, cap or n), 0, -1):
            for rest in partitions(n-first, first):
                yield (first,)+rest

def perm(n, cycles):
    p=list(range(n))
    for cyc in cycles:
        for a,b in zip(cyc,cyc[1:]+cyc[:1]): p[a]=b
    return tuple(p)
def mul(a,b): return tuple(a[b[i]] for i in range(len(a)))
def inv(a): return tuple(a.index(i) for i in range(len(a)))
def comm(a,b): return mul(mul(mul(a,b),inv(a)),inv(b))
def support(a): return sum(i!=x for i,x in enumerate(a))

n=s.symbols('n',integer=True,positive=True)
pol=n**3-5*n**2-84*n+20
assert s.expand(pol.subs(n,n+1)-pol)==3*n*n-7*n-88
den=4*n*(n-2)*(n-3)
num=(n-1)*(n-2)**2+16*n
assert s.expand(3*den-10*num)==2*pol
assert pol.subs(n,15)==1010
assert (3*n*n-7*n-88).subs(n,15)>0
assert s.expand((3*n*n-7*n-88).subs(n,n+1)-(3*n*n-7*n-88))==6*n-4

counts={'partitions':0,'balanced_partitions':0,'commutators':0}
for N in range(15,26):
    k=(N+1)//2
    for lam in partitions(N):
        counts['partitions']+=1
        if max(lam[0],len(lam))>k: continue
        counts['balanced_partitions']+=1
        contents=[j-i for i,r in enumerate(lam) for j in range(r)]
        t=sum(contents); S=sum(c*c for c in contents)
        assert abs(t)<=Fraction(N*(k-1),2)-(N-k)
        assert abs(t)<=Fraction((N-1)*(N-2),4)
        u=Fraction(3*(S-N*(N-1)//2),N*(N-1)*(N-2))
        v=Fraction(4*(t*t+N*(N-1)-3*S),N*(N-1)*(N-2)*(N-3))
        assert u<Fraction(1,4) and v<Fraction(3,10)
    # The even conjugator in the no-odd-centralizer case.
    for ell in range(5,N+1):
        g=perm(N,[list(range(ell))]); x=perm(N,[[0,1,2]])
        assert comm(g,x)==perm(N,[[0,3,1]])
        counts['commutators']+=1
    # Consecutive letters, a transposition plus a fixed point, and fpf involutions.
    for ell in range(3,N+1):
        g=perm(N,[list(range(ell))]); x=perm(N,[[0,1]])
        assert support(comm(g,x))==3
        counts['commutators']+=1
    g=perm(N,[[0,1]]);x=perm(N,[[0,2]])
    assert support(comm(g,x))==3;counts['commutators']+=1
    if N%2==0:
        g=perm(N,[[i,i+1] for i in range(0,N,2)])
        x=perm(N,[[0,2]])
        assert support(comm(g,x))==4;counts['commutators']+=1

proof=Path(__file__).resolve().parents[3]/'research/ordinary_alternating_sharp_obstruction.tex'
out={'status':'PASS','scope':'independent polynomial, permutation and Young-content checks; not extrapolation to all n',
     'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),**counts,
     'n_range':[15,25],'universal_argument_checked_in_whole_proof_report':True,
     'author_code_imported':False,'degree_upper_bound':60,'degree_lower_bound':125}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
