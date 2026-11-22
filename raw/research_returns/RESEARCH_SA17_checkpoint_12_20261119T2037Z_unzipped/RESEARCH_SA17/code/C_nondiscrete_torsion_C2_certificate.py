#!/usr/bin/env python3
"""Exact formal certificate for the two admissible flags in C:nondiscrete-torsion-C2.

The commutative symbols c,d,u represent cI,D,U. Their commutativity is
legitimate here: c is scalar and DU=UD=0. The integral normal form uses
c*d^2=-2*d, c*u=d*u=u^2=0 and 2*u=0. It does not invert 2 or set u=0.
These identities follow in the proof from T0=I+cD, T0^2=I, D in m_A,
m_A J=0, characteristic(B)=2, and T^2=I. The symbolic checks supplement
rather than replace the valuation-domain flag and regular-splitting proof.
"""
from pathlib import Path
import hashlib
import json
import time

START = time.perf_counter()
ROOT = Path(__file__).resolve().parents[1]

class Poly:
    def __init__(self, terms=None):
        result = {}
        for (i,j,k), a in (terms or {}).items():
            if not a or k >= 2 or (k and (i or j)):
                continue
            if k:
                a %= 2
            else:
                r = min(i, max(j-1,0))
                i -= r
                j -= r
                a *= (-2)**r
            key = (i,j,k)
            result[key] = result.get(key,0) + a
        if (0,0,1) in result:
            result[(0,0,1)] %= 2
        self.terms = {key:a for key,a in result.items() if a}
    def __add__(self, other):
        if isinstance(other,int): other=Poly({(0,0,0):other})
        terms=self.terms.copy()
        for key,a in other.terms.items(): terms[key]=terms.get(key,0)+a
        return Poly(terms)
    __radd__ = __add__
    def __neg__(self): return Poly({key:-a for key,a in self.terms.items()})
    def __sub__(self, other): return self + (-other)
    def __mul__(self, other):
        if isinstance(other,int): other=Poly({(0,0,0):other})
        terms={}
        for (i,j,k),a in self.terms.items():
            for (x,y,z),b in other.terms.items():
                key=(i+x,j+y,k+z)
                terms[key]=terms.get(key,0)+a*b
        return Poly(terms)
    __rmul__ = __mul__
    def __eq__(self, other):
        return isinstance(other,Poly) and self.terms==other.terms

zero=Poly()
one=Poly({(0,0,0):1})
c=Poly({(1,0,0):1})
d=Poly({(0,1,0):1})
u=Poly({(0,0,1):1})
t0=one+c*d
t=t0+u

# The nil symbol is retained in the coefficient ring: this is not a
# characteristic-zero rationalization that silently kills all torsion.
assert u != zero
assert 2*u == zero
assert d*d != zero

checks=[]

def scalar(name, value):
    assert value==zero, (name,value.terms)
    checks.append({'identity':name,'formal_entries':1,'status':'PASS'})

def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),zero)
             for j in range(len(b[0]))] for i in range(len(a))]

def matrix(name,a,b):
    count=0
    for i in range(len(a)):
        for j in range(len(a[0])):
            assert a[i][j]==b[i][j], (name,i,j,a[i][j].terms,b[i][j].terms)
            count+=1
    checks.append({'identity':name,'formal_entries':count,'status':'PASS'})

scalar('T0^2=1',t0*t0-one)
scalar('T^2=1',t*t-one)
scalar('cU=0',c*u)
scalar('DU=0',d*u)
scalar('UD=0',u*d)
scalar('T0D=-D',t0*d+d)
scalar('DT0=-D',d*t0+d)
scalar('cD=T0-I',c*d-(t0-one))
scalar('(I+U)^2=I',(one+u)*(one+u)-one)
E=[[t,c],[zero,-t0]]
P=[[one,zero],[-d,one]]
Pinv=[[one,zero],[d,one]]
I=[[one,zero],[zero,one]]
F=[[one+u,c],[zero,-one]]
matrix('E^2=I',mm(E,E),I)
matrix('P Pinv=I',mm(P,Pinv),I)
matrix('Pinv P=I',mm(Pinv,P),I)
matrix('Pinv E P has diagonals I+U and -I',mm(mm(Pinv,E),P),F)

source=ROOT/'notes/C_nondiscrete_torsion_C2_proposed.tex'
result={
 'status':'PASS',
 'statement':'C:nondiscrete-torsion-C2',
 'source':str(source.relative_to(ROOT)),
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'coefficient_ring':'Z[c,d,u]/(c*d^2+2*d,c*u,d*u,u^2,2*u)',
 'torsion_symbol_nonzero_checked':True,
 'checks':checks,
 'identity_count':len(checks),
 'formal_entry_count':sum(x['formal_entries'] for x in checks),
 'scope':'Exact integral symbolic identities for arbitrary-size commuting blocks cI,D,U satisfying the displayed relations. The independent all-rank written proof supplies the small valuation element, regular splitting, and free trivial B-flag.',
 'excluded_claims':['No all-degree polynomiality assertion.','No generic-kernel primary-torsion assumption.','No R-perfect excision theorem asserted.'],
 'runtime_seconds':time.perf_counter()-START,
}
output=ROOT/'logs/C_nondiscrete_torsion_C2_certificate.json'
output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
