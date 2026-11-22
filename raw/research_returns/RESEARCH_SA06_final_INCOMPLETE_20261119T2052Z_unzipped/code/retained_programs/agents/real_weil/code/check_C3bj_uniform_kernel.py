#!/usr/bin/env python3
"""Finite algebra checks for C3bj; not a substitute for its geometric proof."""
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
import json, hashlib
import sympy as s
start=perf_counter(); started=datetime.now(timezone.utc).isoformat()
base=Path(__file__).resolve().parents[1]
checks=[]
def check(name, condition, data):
    ok=bool(condition);checks.append({'name':name,'pass':ok,'data':data})
    if not ok:raise AssertionError(name)
def rank_mod(M,p):
    a=[[int(x)%p for x in row] for row in M.tolist()];nr=len(a);nc=len(a[0]);r=0
    for c in range(nc):
        pivot=next((i for i in range(r,nr) if a[i][c]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r];v=pow(a[r][c],-1,p)
        a[r]=[(v*x)%p for x in a[r]]
        for i in range(nr):
            if i!=r:
                v=a[i][c];a[i]=[(x-v*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==nr:break
    return r
B=s.Matrix([[0,1],[1,0]])
G=s.zeros(8,3);G[2,0]=1;G[3,1]=1;G[6,2]=1
mu=s.zeros(4,4);mu[2,3]=1;mu[3,2]=1
M=s.diag(mu,mu)
t=s.Symbol('t')
primes=[2,3,5,7,11,13,17,19,23,29,31]
for p in primes:
    check(f'cubic_cup_rank_p{p}',rank_mod(B,p)==2,{'determinant_mod_p':int(B.det())%p})
    check(f'incidence_rank_witness_p{p}',rank_mod(G,p)==3 and rank_mod(M*G,p)==3,
          {'section_rank':rank_mod(G,p),'cup_image_rank':rank_mod(M*G,p)})
    q=s.Poly(s.expand((1+t)**p),t,modulus=p)
    first={int(k[0]):int(v)%p for k,v in q.terms() if k[0]<2}
    check(f'square_zero_unit_exponent_p{p}',first=={0:1},{'degree_below_two':first})
h,c,b,d=s.symbols('h c b d')
prod=s.expand((h+c)*(d+b*h))
check('boundary_m1_coefficients',s.expand(prod).coeff(h,0)==c*d and s.expand(prod).coeff(h,1)==d+b*c,
      {'constant':str(prod.coeff(h,0)),'linear':str(prod.coeff(h,1))})
rem=s.expand((c*d).subs(d,-b*c))
check('boundary_m1_substitution',rem==-b*c**2,{'remainder':str(rem)})
A,K=s.symbols('A K')
deg=s.Poly((A+K)**3,A,K).coeff_monomial(A**2*K)*3*4
check('boundary_m1_integer_degree',deg==36,{'degree_over_Z':int(deg),'not_reduced_mod_p':True})
for m in range(2,17):
    check(f'boundary_coefficient_m{m}',prod.coeff(h,2)==b and prod.coeff(h,1)==d+b*c,
          {'h2_coefficient':str(prod.coeff(h,2)),'h_coefficient':str(prod.coeff(h,1))})
check('rank_one_conormal_wedge',s.Matrix([[1,0],[0,1]]).det()==1,
      {'normalization':'dt wedge du corresponds to t tensor du; coefficient one, no division by 2'})
external=[]
for rel in ['../../logs/cubic_surface_line_cup_certificate.json','../frobenius/output/C3bi_cubic_incidence_geometry.json']:
    p=(base/rel).resolve()
    if p.exists():
        external.append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'rerun':False})
result={'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),
        'runtime_seconds':perf_counter()-start,'checks_passed':len(checks),'checks':checks,
        'external_certificates_read_not_rerun':external,
        'scope':'Finite sample of rank-two cup, rank-three open-locus witness, square-zero unit exponent and integral exceptional coefficient identities. Does not certify Bertini, global Picard extension, actual-family descent, Milnor cohomology injection, or all-prime/all-dimension theorem; those are proved in the text.'}
(base/'output/C3bj_uniform_kernel_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
