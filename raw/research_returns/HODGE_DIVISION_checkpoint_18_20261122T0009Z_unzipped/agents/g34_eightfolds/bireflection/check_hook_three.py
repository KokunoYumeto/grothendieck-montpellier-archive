#!/usr/bin/env python3
"""Exact finite supplement for D-HK301--03. No approximate eigenvalues.
All universal proofs are in hook_three_section.tex; finite cases are not
used as a substitute for them. Exterior spectra are explicit root sums.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from collections import Counter
from itertools import combinations
from math import lcm,gcd
import hashlib,json,time,re
import sympy as s

HERE=Path(__file__).resolve().parent
started=datetime.now(timezone.utc).isoformat();timer=time.perf_counter()
def partitions(n,top=None):
    if not n:yield ();return
    for k in range(min(n,top or n),0,-1):
        for pp in partitions(n-k,k):yield (k,)+pp
classes=triples=phase_entries=0;rows=[];least=None
for n in range(15,30):
    a=(n-1)*(n-2)*(n-3)//6
    A=F(n*n-9*n+8,6);B=F(n*n-2*n-1,8);b=F((n-1)**2,8)
    worst=None;typ=None
    for pp in partitions(n):
        L=lcm(*pp)
        roots=[j*(L//length) for length in pp for j in range(length)]
        roots.remove(0)
        assert len(roots)==n-1
        mult=Counter((x+y+z)%L for x,y,z in combinations(roots,3))
        assert sum(mult.values())==a
        triples+=a;phase_entries+=len(mult)
        # Rationality independently forces equality at equal root orders.
        order_mult={}
        for j in range(L):
            order=L//gcd(L,j);m=mult.get(j,0)
            if order in order_mult:assert order_mult[order]==m
            else:order_mult[order]=m
        f=pp.count(1);u=pp.count(2);v=pp.count(3)
        char=F((f-1)*(f-2)*(f-3),6)-(f-1)*u+v
        p1=f-1;p2=f+2*u-1;p3=f+3*v-1
        assert char==F(p1**3-3*p1*p2+2*p3,6) and char>=-b
        I=n-len(pp)
        if I:
            margin=F(a-max(mult.values()))-A*I-B
            assert margin>=0,(n,pp,margin)
            if worst is None or margin<worst:worst=margin;typ=pp
            if least is None or margin<least:least=margin
        else:assert mult=={0:a}
        classes+=1
    rows.append({'n':n,'minimum_support_margin':str(worst),'witness':typ})

# Independent exact signed-subset-cycle computation on selected classes:
# Lambda^3 U = Lambda^3 P - Lambda^2 P + P - 1.
signed_checks=0;signed_orbits=0
for n in range(15,22):
    samples=[(2,)+(1,)*(n-2),(3,)+(1,)*(n-3),(n,),
             (2,)*(n//2)+(1,)*(n%2),(4,)+(1,)*(n-4),(5,3)+(1,)*(n-8)]
    for pp in samples:
        perm=[];offset=0
        for length in pp:
            perm.extend(offset+(j+1)%length for j in range(length));offset+=length
        L=lcm(*pp);out=[0]*(2*L)
        for k,sgn in ((0,-1),(1,1),(2,-1),(3,1)):
            todo=set(combinations(range(n),k))
            while todo:
                first=next(iter(todo));word=first;sign=1;length=0
                while word in todo:
                    todo.remove(word);length+=1
                    im=tuple(perm[i] for i in word)
                    inv=sum(im[i]>im[j] for i in range(k) for j in range(i+1,k))
                    sign*=(-1)**inv;word=tuple(sorted(im))
                assert word==first and L%length==0
                for j in range(length):
                    exponent=(2*j+(sign==-1))*(L//length)
                    out[exponent%(2*L)]+=sgn
                signed_orbits+=1
        roots=[j*(L//length) for length in pp for j in range(length)]
        roots.remove(0);expected=Counter((2*(x+y+z))%(2*L) for x,y,z in combinations(roots,3))
        assert out==[expected.get(j,0) for j in range(2*L)]
        assert min(out)>=0;signed_checks+=1

n,f,x,t=s.symbols('n f x t')
a=(n-1)*(n-2)*(n-3)/6
A=(n*n-9*n+8)/6;B=(n*n-2*n-1)/8;b=(n-1)**2/8
c=(n*n-6*n+8)/6;cf=(f*f+(n-6)*f+n*n-6*n+9)/6
upper=(f-1)*(f-2)*(f-3)/6+(n-f)/3
assert s.expand(a-upper-(n-f)*cf)==0
assert s.expand(a-n/2+1-n*c)==0
assert s.expand(cf-c-(f*f+(n-6)*f+1)/6)==0
p=(n-f)*(f*f+(n-6)*f+3*n+1)-3*n*(n-2)
assert s.expand(12*((cf-A)*(n-f)/2-b-B)-p)==0
assert s.expand(p-(-f**3+6*f*f+(n*n-9*n-1)*f+7*n))==0
assert s.expand(s.diff(p,f,2)-(12-6*f))==0
assert s.expand(p.subs(f,2)-(2*n*n-11*n+14))==0
assert s.expand(p.subs(f,n-2)-(n*n-12*n+34))==0
assert s.expand(2*A*(n-1)+12*B-2*a-(n*n-6*n-13)/6)==0
assert s.expand(2*A*(n-1)-2*a+2*(n-1)*(2*n-1)/3)==0
assert s.expand(18*B-2*(n-1)*(2*n-1)/3-2-(11*n*n-30*n-59)/12)==0
positive=[p.subs(f,2),p.subs(f,n-2),(n*n-6*n-13)/6-6,
          A+B-40,A+B-b,a-1-2*(A+B),a-B,
          18*B-2*(n-1)*(2*n-1)/3-2]
for expr in positive:
    poly=s.Poly(s.expand(expr.subs(n,x+15)),x)
    assert all(v>=0 for v in poly.all_coeffs()) and poly.eval(0)>0
# Check precisely the three translated numerators printed in HK3.15.
assert s.expand(24*(A+B-40).subs(n,x+15)-(7*x*x+168*x+14))==0
assert s.expand(12*(A+B-b).subs(n,x+15)-(2*x*x+42*x+193))==0
assert s.expand(12*(a-1-2*(A+B)).subs(n,x+15)-(2*x**3+71*x*x+844*x+3382))==0
proof=HERE/'hook_three_section.tex';text=proof.read_text()
assert not any(ord(ch)<32 and ch not in '\n\t\r' for ch in text)
assert text.count('\\[')==text.count('\\]')==20
tags=re.findall(r'\\tag\{([^}]+)\}',text);assert len(tags)==len(set(tags))==20
assert text.count('\\begin{proof}')==text.count('\\end{proof}')==3
assert not re.search(r'(?<!\\)qquad',text)
result={'status':'PASS','started_utc':started,'completed_utc':datetime.now(timezone.utc).isoformat(),
 'elapsed_seconds':time.perf_counter()-timer,'all_partition_classes':classes,
 'explicit_exterior_eigenvalue_triples':triples,'distinct_phase_entries':phase_entries,
 'signed_subset_crosschecks':signed_checks,'actual_signed_subset_orbits':signed_orbits,
 'minimum_support_margin':str(least),'universal_positive_polynomials':len(positive),
 'rows':rows,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'scope':'Exact spectra and symbolic identities supplement the universal proof; no finite source-existence or universal sufficiency inference.'}
(HERE/'hook_three_checked.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
