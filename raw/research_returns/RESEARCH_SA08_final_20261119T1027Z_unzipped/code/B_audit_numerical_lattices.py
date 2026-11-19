"""Independent audit of A-017: Fraction-polynomial wedge arithmetic.

Regenerates all twelve reported lattices without importing the root program.
The HNF/SNF backend is shared (SymPy); polynomial, derivative, wedge and
generator enumeration are independently implemented. Also checks finite
instances of the mod-p evaluation/periodicity argument, including negatives.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product, combinations
from functools import lru_cache
from math import comb, factorial, lcm
import json, time
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.domains import ZZ

base = Path(__file__).resolve().parents[1]
started = time.monotonic()
old = json.loads((base/'logs/A_numerical_differentials.json').read_text())

def indices(d, bound):
    return [e for e in product(range(bound+1), repeat=d) if sum(e)<=bound]

def add_term(out, key, value):
    out[key] = out.get(key, Q(0)) + value
    if not out[key]: del out[key]

def multiply(a, b):
    out = {}
    for ea, va in a.items():
        for eb, vb in b.items():
            add_term(out, tuple(x+y for x,y in zip(ea,eb)), va*vb)
    return out

@lru_cache(None)
def beta(e):
    d=len(e); zero=(0,)*d
    out={zero:Q(1)}
    for j, power in enumerate(e):
        unit=tuple(int(i==j) for i in range(d))
        for r in range(power):
            out=multiply(out,{unit:Q(1),zero:Q(-r)})
        out={m:c/factorial(power) for m,c in out.items()}
    return out

def differential(poly):
    out={}
    for e,c in poly.items():
        for j in range(1,len(e)): # relative to T
            if e[j]:
                f=list(e);f[j]-=1
                add_term(out,((j,),tuple(f)),c*e[j])
    return out

def wedge(a,b):
    out={}
    for (ia,ea),ca in a.items():
        for (ib,eb),cb in b.items():
            if set(ia)&set(ib): continue
            sign=(-1)**sum(x>y for x in ia for y in ib)
            key=(tuple(sorted(ia+ib)),tuple(x+y for x,y in zip(ea,eb)))
            add_term(out,key,sign*ca*cb)
    return out

audit=[]; previous={}; total_tuples=0
for record in old['records']:
    n,q,w=(record[k] for k in ('relative_dimension','form_degree','weight'))
    d=n+1
    ambient=[(i,e) for i in combinations(range(1,d),q) for e in indices(d,w-q)]
    assert set(ambient)=={(tuple(i),tuple(e)) for e,i in record['monomial_wedge_basis']}
    positions={key:j for j,key in enumerate(ambient)}
    small=indices(d,w)
    positives=[e for e in small if any(e)]
    columns=[]; count=0
    for bs in product(positives,repeat=q):
        remaining=w-sum(sum(b) for b in bs)
        if remaining<0: continue
        form={((),(0,)*d):Q(1)}
        for b in bs: form=wedge(form,differential(beta(b)))
        for a in indices(d,remaining):
            count+=1
            full=wedge({((),e):c for e,c in beta(a).items()},form)
            if not full: continue
            column=[Q(0)]*len(ambient)
            for key,c in full.items(): column[positions[key]]=c
            columns.append(column)
    total_tuples+=count
    assert count==record['generator_tuples']
    assert len(columns)==record['nonzero_generators']
    den=lcm(*(c.denominator for col in columns for c in col))
    mat=sp.Matrix.hstack(*(sp.Matrix([int(c*den) for c in col]) for col in columns))
    own=hermite_normal_form(mat)/den
    reported=sp.Matrix.hstack(*(sp.Matrix(col) for col in record['hnf_columns_after_denominator']))/record['common_denominator']
    # Same finite monomial ordering as the mathematical cartesian construction.
    assert own.rows==own.cols==len(ambient)
    change=own.inv()*reported
    inverse=reported.inv()*own
    assert all(v.q==1 for v in change) and all(v.q==1 for v in inverse)
    assert abs(change.det())==1
    if (n,q) in previous:
        oldambient,oldbasis=previous[(n,q)]
        embedded=sp.zeros(len(ambient),len(oldambient))
        for j,key in enumerate(oldambient): embedded[positions[key],:]=oldbasis[j,:]
        inclusion=own.inv()*embedded
        assert all(v.q==1 for v in inclusion)
        diagonal=smith_normal_form(inclusion,domain=ZZ)
        diag=[abs(int(diagonal[j,j])) for j in range(min(diagonal.shape))]
    else: diag=[]
    rank=sum(bool(v) for v in diag)
    torsion=[v for v in diag if v>1]
    assert len(ambient)-rank==record['free_rank']
    assert torsion==record['torsion_invariants']
    audit.append(dict(n=n,q=q,w=w,tuples=count,free_rank=len(ambient)-rank,torsion=torsion))
    previous[(n,q)]=(ambient,own)

def binomial_integer(x,a):
    return comb(x,a) if x>=0 else (-1)**a*comb(a-x-1,a)

prime_cases=[]; periodic_checks=0
for p,r in ((2,1),(2,2),(2,3),(3,1),(3,2),(5,1)):
    m=p**r
    evaluation=sp.Matrix([[binomial_integer(x,a)%p for a in range(m)] for x in range(m)])
    assert evaluation.det()%p==1
    for a in range(m):
        for x in range(-2*m,2*m+1):
            assert (binomial_integer(x+m,a)-binomial_integer(x,a))%p==0
            periodic_checks+=1
    prime_cases.append(dict(prime=p,r=r,size=m,determinant_mod_p=1))

out=dict(status='all independent audit assertions passed',lattice_cases=len(audit),
    generator_tuples=total_tuples,periodicity_checks=periodic_checks,
    seconds=time.monotonic()-started,lattices=audit,prime_cases=prime_cases,
    limitations='Finite checks only; the all-degree cotangent and filtration proof is audited in notes/B_A017_audit.md.')
(base/'logs/B_audit_numerical_lattices.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
