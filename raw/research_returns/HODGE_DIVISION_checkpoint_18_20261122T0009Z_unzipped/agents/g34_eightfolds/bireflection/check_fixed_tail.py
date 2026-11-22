"""Exact coefficient and constant supplement for D-AFT01--03.

The general proof is written separately. This finite program constructs
character polynomials from the published recursive umbral formula, checks
their structural premises and effective thresholds, and independently
matches degrees with the hook formula. It does not sample enormous S_n.
"""
from pathlib import Path
from datetime import datetime,timezone
from functools import lru_cache
from collections import Counter
from math import factorial
import hashlib,json,time
import sympy as s

ROOT=Path(__file__).resolve().parent
START=time.perf_counter();STAMP=datetime.now(timezone.utc).isoformat()
X=s.symbols('x1:9')

def parts(n,top=None):
    if n==0:
        yield ();return
    for a in range(min(n,top or n),0,-1):
        for rest in parts(n-a,a):yield (a,)+rest

def hooks_degree(shape):
    numerator=factorial(sum(shape));denominator=1
    for i,row in enumerate(shape):
        for j in range(row):
            denominator*=row-j+sum(r>j for r in shape[i+1:])
    assert numerator%denominator==0
    return numerator//denominator

@lru_cache(None)
def falling(i,r):
    return s.prod(X[i]-j for j in range(r))

@lru_cache(None)
def q(shape):
    if not shape:return s.Integer(1)
    k=sum(shape);tail=q(shape[1:]);raw=s.Integer(0)
    for alpha in parts(k):
        counts=Counter(alpha)
        value=tail.subs({X[i]:counts[i+1] for i in range(8)})
        z=s.prod(i**a*factorial(a) for i,a in counts.items())
        raw+=value/z*s.prod(((i*X[i-1]-1)**a) for i,a in counts.items())
    raw=s.Poly(s.expand(raw),*X)
    answer=s.Integer(0)
    for exponents,coefficient in raw.terms():
        answer+=coefficient*s.prod(falling(i,r) for i,r in enumerate(exponents))
    return s.expand(answer)

f,v=X[0],X[2]
assert s.expand(q((3,))-(f*(f-1)*(f-5)/6+(f-1)*X[1]+v))==0
assert s.expand(q((2,1))-(f*(f-2)*(f-4)/3-v))==0
assert s.expand(q((1,1,1))-((f-1)*(f-2)*(f-3)/6-(f-1)*X[1]+v))==0

rows=[];monomials=dimension_checks=0
for k in range(3,9):
    for shape in parts(k):
        poly=s.Poly(q(shape),*X)
        C=s.Rational(hooks_degree(shape),factorial(k))
        leading=(k,)+(0,)*7
        assert poly.coeff_monomial(leading)==C>0
        others=[]
        for exponents,coefficient in poly.terms():
            weighted=sum((i+1)*a for i,a in enumerate(exponents))
            assert weighted<=k
            if sum(exponents)==k:assert exponents==leading
            if exponents!=leading:others.append(abs(coefficient))
            if any(exponents[1:]):
                assert sum(exponents)<=k-1
                assert exponents[0]+2*sum(exponents[1:])<=k
            monomials+=1
        M=1+sum(others)/C
        F=int(s.ceiling(k*M))+1
        bounds=[2*k+2,200,100/C,100*k*M,
                (100*(1+M))**5,(100*(1+M)*F**k)**2]
        N=int(s.ceiling(max(bounds)))
        assert all(N>=x for x in bounds)
        assert F>k*M and M>=1
        degree=s.Poly(poly.as_expr().subs({x:0 for x in X[1:]}),f)
        for n in [2*k+2,3*k+1,5*k+3]:
            assert degree.eval(n)==hooks_degree((n-k,)+shape)
            dimension_checks+=1
        a=degree.eval(N);S=C*N**(k-1)
        A=a/N-s.Rational(101,100)*C*N**(k-2)
        B=s.Rational(2,5)*S;b=S/100;d0=A+B
        assert S>=100
        assert s.Rational(99,100)*N*S<=a<=s.Rational(101,100)*N*S
        assert s.Rational(9,10)*S<=A<=s.Rational(101,100)*S
        assert s.Rational(13,10)*S<=d0<=s.Rational(141,100)*S
        assert b<=d0 and 2*d0<=a-1 and B>=40
        assert 2*A*(N-1)+12*B-2*a>=s.Rational(19,25)*S>6
        assert 18*B+2*A*(N-1)-2*a-2>=s.Rational(79,25)*S-2>0
        rows.append({'mu':shape,'C':str(C),'M':str(M),'F':F,'N':str(N),
                     'N_digits':len(str(N)),'monomials':len(poly.terms()),
                     'character_polynomial':str(poly.as_expr())})

# Universal rational margins, separate from the finite polynomial list.
assert s.Rational(9,20)-s.Rational(1,100)==s.Rational(11,25)>s.Rational(2,5)
assert 5*s.Rational(9,100)-s.Rational(1,100)==s.Rational(11,25)
assert s.Rational(89,100)-s.Rational(1,100)>s.Rational(2,5)
assert s.Rational(99,100)-s.Rational(101,20000)>s.Rational(9,10)
assert s.Rational(24,5)-s.Rational(101,25)==s.Rational(19,25)
assert s.Rational(36,5)-s.Rational(101,25)==s.Rational(79,25)
assert s.Rational(99,100)*200*100-1>2*s.Rational(141,100)*100
for k in range(3,201):
    assert s.Rational(3*k,5)-(k-1)<=-s.Rational(1,5)
    assert s.Rational(k+1,2)<=k-1

proof=ROOT/'fixed_tail_section.tex'
text=proof.read_text()
assert 'D-AFT01' in text and 'D-AFT03' in text
assert text.count('\\begin{proof}')==text.count('\\end{proof}')==3
assert text.count('\\[')==text.count('\\]')
assert text.count('\\begin{theorem}')==text.count('\\end{theorem}')==3
tags=__import__('re').findall(r'\\tag\{([^}]+)\}',text)
assert len(tags)==len(set(tags))==20
for env in ['gathered','aligned','split']:
    chunks=__import__('re').findall(r'\\begin\{'+env+r'\}(.*?)\\end\{'+env+r'\}',text,__import__('re').S)
    assert all('\\tag' not in chunk for chunk in chunks)
out={'status':'PASS','started_utc':STAMP,
     'completed_utc':datetime.now(timezone.utc).isoformat(),
     'elapsed_seconds':time.perf_counter()-START,
     'tail_partitions':len(rows),'coefficient_monomials':monomials,
     'independent_hook_degree_matches':dimension_checks,
     'known_tail_three_polynomials':3,'rows':rows,
     'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
     'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Exact finite polynomial premises and explicit threshold arithmetic; universal inequalities and actual cover argument are proved in the separate full text.'}
(ROOT/'fixed_tail_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({key:value for key,value in out.items() if key!='rows'},indent=2))
