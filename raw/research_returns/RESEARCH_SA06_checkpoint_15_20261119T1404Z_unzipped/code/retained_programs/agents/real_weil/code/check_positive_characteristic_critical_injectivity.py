#!/usr/bin/env python3
"""Exact finite certificates for C.3ay, separate from its universal proof.

Finite-field geometry checks only the constant elliptic curve and its
horizontal-line base.  Infinite order is proved by the generic-point
argument, never inferred from a finite-field point.  Integral Chow-ring
identities are checked over Z, including coefficients divisible by p.
"""
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter
from itertools import product
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

started=perf_counter();base=Path(__file__).resolve().parent
u,U,V,W=S.symbols('u U V W')

def constants(p,r):
    for e in range(1,10):
        phi=None
        for cs in product(range(p),repeat=e):
            candidate=u**e+sum(c*u**(e-1-i) for i,c in enumerate(cs))
            if S.Poly(candidate,u,modulus=p).is_irreducible:
                phi=candidate;break
        assert phi is not None
        def red(f):return S.rem(S.expand(f),phi,u,modulus=p)
        good=[]
        for cs in product(range(p),repeat=e):
            c=sum(a*u**(e-1-i) for i,a in enumerate(cs))
            test=c*c+c if p==2 else 4-27*c**4
            if red(test)!=0:good.append(c)
            if len(good)==r:return e,phi,good,red
    raise AssertionError('finite sample search exhausted')

curve_checks=[];geometry=[]
for p in [2,3,5,7,11,13]:
    F=V**2*W+V*W**2+U**3 if p==2 else V**2*W-U**3+U*W**2
    charts=[]
    for t in [U,V,W]:
        vars=tuple(z for z in [U,V,W] if z!=t)
        eq=[S.expand(g.subs(t,1)) for g in [F,S.diff(F,U),S.diff(F,V),S.diff(F,W)]]
        gb=S.groebner(eq,*vars,modulus=p)
        ok=len(gb.polys)==1 and gb.polys[0].as_expr()==1
        assert ok;charts.append(ok)
    curve_checks.append({'p':p,'equation':str(F),'all_projective_jacobian_charts_unit':charts})
    for r in [2,3,4,6]:
        e,phi,bs,red=constants(p,r)
        separability=[];determinants=[]
        for i,c in enumerate(bs):
            f=U**3+c*c+c if p==2 else U**3-U-c*c
            gb=S.groebner([f,S.diff(f,U),phi],U,u,modulus=p)
            ok=len(gb.polys)==1 and gb.polys[0].as_expr()==1
            assert ok;separability.append(ok)
            det=red(S.prod(c-d for j,d in enumerate(bs) if j!=i))
            assert det!=0;determinants.append(str(det))
        assert all(red(a-b)!=0 for i,a in enumerate(bs) for b in bs[i+1:])
        geometry.append({'p':p,'r':r,'extension_degree':e,'field_polynomial':str(phi),
                         'constants':[str(b) for b in bs],
                         'horizontal_cubic_separability':separability,
                         'base_jacobian_determinants_in_etale_V_coordinate':determinants,
                         'reduced_base_length':3*r,'local_dimension':2*r,'passed':True})

h,a,y,c=S.symbols('h a y c');chern=[]
for r in range(2,31):
    top=sum((-h)**j*a**(r-1-j) for j in range(r))
    assert S.expand(top.subs(h,-a)-r*a**(r-1))==0
    remainder=S.rem(S.expand((y+c)**r-y**r),c**2,c)
    assert S.expand(remainder-r*y**(r-1)*c)==0
    chern.append({'r':r,'regular_section_rank':r-1,'chern_sum_at_h_minus_a':str(r*a**(r-1)),
                  'integral_eliminated_relation':str(remainder),'passed':True})

def basis(r,d):
    return [(i,j,t) for i in range(r) for j in range(r) for t in ['1','degree','lambda']
            if i+j+(t!='1')==d]

quotients=[]
for r in range(2,16):
    src=basis(r,r-1);dst=basis(r,r);index={v:i for i,v in enumerate(dst)}
    matrix=S.zeros(len(dst),len(src))
    for j,(i,k,t) in enumerate(src):
        for mon,coef in [((i+1,k,t),1),((i,k+1,t),1)]+([((i,k,'degree'),3)] if t=='1' else []):
            if mon in index:matrix[index[mon],j]+=coef
    snf=smith_normal_form(matrix,domain=ZZ)
    diag=[abs(int(snf[i,i])) for i in range(min(snf.shape)) if snf[i,i]!=0]
    assert len(dst)-len(diag)==1
    assert [d for d in diag if d!=1]==[3*r]
    functional=S.Matrix([[(-1)**i if t=='lambda' else 0 for i,j,t in dst]])
    assert functional*matrix==S.zeros(1,len(src))
    witness=S.zeros(len(dst),1);witness[index[(0,r-1,'lambda')],0]=r
    assert (functional*witness)[0,0]==r
    quotients.append({'r':r,'formal_Pic_model':'Z degree + Z lambda, M=3 degree',
                      'source_relations_rank':len(diag),'free_quotient_rank':1,
                      'nonunit_Smith_factors':[d for d in diag if d!=1],
                      'lambda_functional_on_witness':r,'passed':True})

record={'timestamp_utc':datetime.now(timezone.utc).isoformat(),
        'curve_checks':curve_checks,'constant_base_geometry':geometry,
        'integral_Chern_identities':chern,'integral_quotient_models':quotients,
        'counts':{'elliptic_curves':len(curve_checks),'constant_base_cases':len(geometry),
                  'Chern_identity_cases':len(chern),'integral_quotient_models':len(quotients)},
        'scope':'Finite exact certificates. The universal geometry, actual families, strict-local injection and generic-point infinite order are proved in the text.',
        'runtime_seconds':perf_counter()-started}
(base/'check_positive_characteristic_critical_injectivity_output.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
