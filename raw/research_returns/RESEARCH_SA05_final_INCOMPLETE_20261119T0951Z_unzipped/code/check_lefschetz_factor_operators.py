"""Exact sl2-string checks for the proposed motivated C6 extension.

These are operator identities over Q, not checks of geometric comparison.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import time
import sympy as sp

start=time.perf_counter()

def exp_nilpotent(a):
    out=sp.eye(a.rows)
    term=sp.eye(a.rows)
    for j in range(1,a.rows+1):
        term=term*a/j
        out+=term
    assert term==sp.zeros(a.rows)
    return out

def string(d,i):
    n=d-i
    l=sp.zeros(n+1); low=sp.zeros(n+1); star=sp.zeros(n+1)
    degrees=[i+2*k for k in range(n+1)]
    for k in range(n+1):
        if k<n: l[k+1,k]=1
        if k: low[k-1,k]=k*(n-k+1)
        star[n-k,k]=(-1)**(i*(i+1)//2)*sp.factorial(k)/sp.factorial(n-k)
    sign=sp.diag(*[(-1)**(m*(m+1)//2) for m in degrees])
    w=exp_nilpotent(l)*exp_nilpotent(-low)*exp_nilpotent(l)
    assert star*star==sp.eye(n+1)
    assert star*l*star==low
    assert w*sign==star
    assert low*l-l*low==sp.diag(*[d-m for m in degrees])
    return l,low,star,degrees

models={}
for d in range(6):
    for i in range(d+1): models[d,i]=string(d,i)

checks=[]
for dx in range(4):
    for ix in range(dx+1):
        for dy in range(4):
            for iy in range(dy+1):
                lx,ax,sx,mx=models[dx,ix]
                ly,ay,sy,my=models[dy,iy]
                lxp=sp.kronecker_product(lx,sp.eye(ly.rows))
                axp=sp.kronecker_product(ax,sp.eye(ly.rows))
                lyp=sp.kronecker_product(sp.eye(lx.rows),ly)
                ayp=sp.kronecker_product(sp.eye(lx.rows),ay)
                l=lxp+lyp; a=axp+ayp
                total_degrees=[m+n for m in mx for n in my]
                sign=sp.diag(*[(-1)**(m*(m+1)//2) for m in total_degrees])
                total_star=exp_nilpotent(l)*exp_nilpotent(-a)*exp_nilpotent(l)*sign
                cross=sp.diag(*[(-1)**(m*n) for m in mx for n in my])
                assert total_star==sp.kronecker_product(sx,sy)*cross
                assert total_star*lxp*total_star==axp
                assert total_star*lyp*total_star==ayp
                hx=axp*lxp-lxp*axp
                # Recover each degree projector by a universal polynomial in h_X.
                for m in range(2*dx+1):
                    proj=sp.eye(hx.rows)
                    target=dx-m
                    for mm in range(2*dx+1):
                        if mm!=m:
                            node=dx-mm
                            proj=proj*(hx-node*sp.eye(hx.rows))/(target-node)
                    expected=sp.diag(*[int(a_degree==m) for a_degree in mx for _ in my])
                    assert proj==expected
                checks.append(dict(dx=dx,ix=ix,dy=dy,iy=iy,dimension=l.rows))

l,a,h,_=models[2,0]
lef=sp.zeros(3)
for k in range(3): lef[2-k,k]=1
source_discrepancy=dict(
    example='P2, basis (1,L,L^2), input L',
    lefschetz_star_conjugate=list(lef*l*lef*sp.Matrix([0,1,0])),
    hodge_star_conjugate=list(h*l*h*sp.Matrix([0,1,0])),
    conclusion='The two conjugates in the printed p11 equality differ: 1 versus 2 on L. The Hodge-star conjugate equals the normalized lowering operator, as directly follows from p10.'
)
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='passed',
    scope='Exact rational sl2 identities only, no geometric spectral-sequence assertion.',
    single_strings=len(models),tensor_string_cases=checks,
    source_discrepancy=source_discrepancy,
    seconds=round(time.perf_counter()-start,6),sympy_version=sp.__version__)
Path(__file__).with_name('check_lefschetz_factor_operators_output.json').write_text(
    json.dumps(result,indent=2,default=str)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='tensor_string_cases'},indent=2,default=str))
print('Passed',len(checks),'tensor-string cases.')
