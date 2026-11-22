#!/usr/bin/env python3
"""Independent supplement to ATT04--06, using actual signed pair orbits."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from itertools import combinations
from math import lcm,gcd
import ast,datetime,hashlib,json,time
import sympy as s

start=time.perf_counter();here=Path(__file__).resolve().parent
proof=here.parents[1]/'g34_eightfolds/bireflection/alternating_two_factor_section.tex'
assert hashlib.sha256(proof.read_bytes()).hexdigest()=='b7a5a8d6e9c887fb0e3cdb4964bd2cda6a927d38d8d314b2c821cb3f4c78bcbf'
# Reuse ONLY the two pure functions from this auditor's preceding
# independently authored actual-orbit checker.  No author code or
# top-level test/output side effects are executed.
own_source=here.parent/'audit_alternating_two_tail/independent_check.py'
tree=ast.parse(own_source.read_text())
fns=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('partitions','actual_spectra')]
assert len(fns)==2
exec(compile(ast.Module(body=fns,type_ignores=[]),str(own_source),'exec'))

rows=0;entry_checks=0
for n in range(15,27):
    A=F(n-5,2);B=F(n,4)
    for partition in partitions(n):
        L,specs,traces,orbits=actual_spectra(partition)
        k=n-len(partition)
        if k:
            for spec in specs:
                a=sum(spec.values())
                assert a-max(spec.values())>=A*k+B
                entry_checks+=len(spec)
        rows+=1

# Build actual weighted swaps on eigenbasis words, without the author's
# aggregate N_zeta formula, then compare against that independently
# derived multiplicity identity and support bound.
swap_cases=0;swap_eigenvalue_checks=0
for n in range(15,23):
    chosen=[(1,)*n,(2,)+(1,)*(n-2),(3,)+(1,)*(n-3),
            (4,)+(1,)*(n-4),(5,)+(1,)*(n-5),(n,),
            (2,)*(n//2)+(1,)*(n%2)]
    for part in chosen:
        L,specs,_,_=actual_spectra(part)
        for spec in specs:
            roots=list(spec.elements());a=len(roots)
            result=Counter()
            for i,x in enumerate(roots):
                result[2*x%(2*L)]+=1
                for y in roots[i+1:]:
                    result[(x+y)%(2*L)]+=1
                    result[(x+y+L)%(2*L)]+=1
            assert sum(result.values())==a*a
            nu=a-max(spec.values())
            for z in range(2*L):
                count=sum(mult*spec[(z-x)%L] for x,mult in spec.items())
                plus=spec[z//2] if z%2==0 else 0
                zm=(z+L)%(2*L)
                minus=spec[zm//2] if zm%2==0 else 0
                assert 2*result[z]==count+plus-minus
                assert 2*(a*a-result[z])>=a*a+a*nu-a
                swap_eigenvalue_checks+=1
            if part==(1,)*n:
                assert set(result)=={0,L}
            swap_cases+=1

# Direct actual imprimitive cycles for all pairs of permutations
# x,y in S4, not merely a chosen cycle product representative.
from itertools import permutations
index_cases=0
def compose(x,y):return tuple(x[y[i]] for i in range(len(x)))
def cycles(p):
    seen=set();lengths=[]
    for x in range(len(p)):
        if x in seen:continue
        y=x;l=0
        while y not in seen:seen.add(y);l+=1;y=p[y]
        lengths.append(l)
    return sorted(lengths)
for x in permutations(range(4)):
    for y in permutations(range(4)):
        # (x,y) times block swap sends first block via y to second.
        natural=tuple(4+y[i] for i in range(4))+tuple(x[i] for i in range(4))
        h=compose(x,y)
        assert cycles(natural)==[2*l for l in cycles(h)]
        assert 8-len(cycles(natural))==4+(4-len(cycles(h)))
        index_cases+=1

# Universal identities and lower bounds, with n=15+u and u>=0.
n,u=s.symbols('n u',integer=True,nonnegative=True)
A=(n-5)/2;B=n/4
assert s.expand(A*(2*n-2)+12*B-(n*n-3*n+5))==0
symbolic=[]
for kind,a,d0,b_bound in [('UP',n*(n-3)/2,n-3,1),
                         ('EX',(n-1)*(n-2)/2,n-2,(n-1)/2)]:
    final=(s.Rational(3,2) if kind=='UP' else s.Rational(1,2))*a
    conditions=[a*(8*d0-2)-6,a*(9*d0-s.Rational(1,2)*(b_bound+1))-6,
                a-B+1,final-6]
    for expression in conditions:
        coefficients=s.Poly(s.expand(expression.subs(n,u+15)),u).all_coeffs()
        assert all(v.is_Rational and v>0 for v in coefficients)
    symbolic.append({'kind':kind,'positive_shifted_polynomials':len(conditions)})

# Irreducibility of the actual A_n constituents can additionally be
# checked by the stable factorial moment calculation (n>=6).  For
# r+2s<=4, E[(f1)_r(f2)_s]=2^-s on A_n, since the unprescribed
# letters leave at least two letters with both possible parities.
x,y=s.symbols('x y')
def expectation(poly):
    poly=s.Poly(s.expand(poly),x,y);ans=0
    for (i,j),coefficient in poly.terms():
        for r in range(i+1):
            for z in range(j+1):
                ans+=coefficient*s.functions.combinatorial.numbers.stirling(i,r,kind=2)*s.functions.combinatorial.numbers.stirling(j,z,kind=2)*s.Rational(1,2)**z
    return s.simplify(ans)
for chi in (x*(x-3)/2+y,(x-1)*(x-2)/2-y):
    assert expectation(chi)==0 and expectation(chi**2)==1

out={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'elapsed_seconds':time.perf_counter()-start,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'own_orbit_dependency_sha256':hashlib.sha256(own_source.read_bytes()).hexdigest(),
 'common_index_partitions_n15_26':rows,'common_index_spectral_entries':entry_checks,
 'actual_weighted_swap_cases':swap_cases,'swap_eigenvalue_checks':swap_eigenvalue_checks,
 'actual_two_permutation_block_cases':index_cases,'universal_polynomial_checks':symbolic,
 'alternating_character_inner_products':'both one; both trivial multiplicities zero',
 'scope':'Separate exact finite and symbolic supplement; universal scalar/normalizer/cover argument reviewed in full.'}
(here/'independent_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
